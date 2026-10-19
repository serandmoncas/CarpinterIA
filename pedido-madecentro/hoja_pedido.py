"""Convierte una lista de corte CSV en una hoja de pedido imprimible para Madecentro.

Uso: python3 pedido-madecentro/hoja_pedido.py despieces/nochero.csv --cliente "Carlos" > pedido.html
Se abre en el navegador y se imprime o se guarda como PDF.

Con --madecentro DIR además escribe un CSV por material con las columnas del optimizador
de Madecentro (tablerosmadecentro.com), que escoge el tablero una vez por optimización.
"""

import argparse
import csv
import html
import math
import sys
from datetime import date
from pathlib import Path

# Formatos de tablero que se consiguen en Colombia (ancho × largo, mm). Cambian según la marca:
# Pelikano y la melamina RH de Arauco vienen en 2150 × 2440, Kronospan en 2070 × 2800.
FORMATOS = [(1830, 2440), (2150, 2440), (1830, 2500), (2070, 2800)]
REFILADO = 20  # mm que la planta recorta por eje antes de cortar (valor por defecto de Madecentro)

COLUMNAS_MADECENTRO = ["Ancho (mm)", "Alto (mm)", "Cantidad", "Descripción", "Veta",
                       "Canto Superior", "Canto Inferior", "Canto Izquierdo", "Canto Derecho",
                       "Servicios"]
VETA_MADECENTRO = {"vertical": "Vertical", "largo": "Vertical", "l": "Vertical",
                   "horizontal": "Horizontal", "ancho": "Horizontal", "a": "Horizontal"}


def leer_piezas(ruta: str) -> list[dict]:
    with open(ruta, encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def totales(piezas: list[dict]) -> dict:
    """Área en m² por material y metros lineales de tapacanto."""
    area: dict[str, float] = {}
    tapacanto_mm = 0
    for p in piezas:
        cantidad, largo, ancho = int(p["cantidad"]), int(p["largo"]), int(p["ancho"])
        material = f'{p["color"]} {p["espesor"]} mm'
        area[material] = area.get(material, 0) + cantidad * largo * ancho / 1_000_000
        cantos = (int(p["L1"]) + int(p["L2"])) * largo + (int(p["A1"]) + int(p["A2"])) * ancho
        tapacanto_mm += cantidad * cantos
    return {"area": area, "tapacanto_m": tapacanto_mm / 1000}


def uso_tableros(area_m2: float) -> list[tuple[str, float, int]]:
    """Para cada formato: nombre, fracción del área útil que se usa y tableros mínimos.

    Es una cota por área: el número real sale del optimizador, porque el corte de sierra
    y las piezas que no encajan dejan sobrantes.
    """
    resultado = []
    for ancho, largo in FORMATOS:
        util = (ancho - REFILADO) * (largo - REFILADO) / 1_000_000
        resultado.append((f"{ancho} × {largo}", area_m2 / util, math.ceil(area_m2 / util)))
    return resultado


def pedido_madecentro(piezas: list[dict]) -> dict[str, list[list[str]]]:
    """Filas del optimizador de Madecentro, agrupadas por material.

    Alto es el largo de la pieza, así que los cantos largos (L1, L2) quedan a izquierda y
    derecha y los anchos (A1, A2) arriba y abajo. Cada canto lleva el color de la pieza.
    Las notas van en Servicios, porque es lo único que la planta lee además de las medidas.
    """
    por_material: dict[str, list[list[str]]] = {}
    for p in piezas:
        canto = lambda lado: p["color"] if p[lado] == "1" else ""
        fila = [p["ancho"], p["largo"], p["cantidad"], p["pieza"],
                VETA_MADECENTRO.get(p["veta"].strip().lower(), ""),
                canto("A1"), canto("A2"), canto("L1"), canto("L2"), p["notas"]]
        por_material.setdefault(f'{p["color"]} {p["espesor"]} mm', []).append(fila)
    return por_material


def escribir_madecentro(piezas: list[dict], carpeta: str, proyecto: str) -> list[Path]:
    rutas = []
    Path(carpeta).mkdir(parents=True, exist_ok=True)
    for material, filas in pedido_madecentro(piezas).items():
        nombre = f"{proyecto}-{material}".lower().replace(" ", "-")
        ruta = Path(carpeta) / f"{nombre}.csv"
        # utf-8-sig para que Excel abra bien las tildes
        with open(ruta, "w", encoding="utf-8-sig", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(COLUMNAS_MADECENTRO)
            escritor.writerows(filas)
        rutas.append(ruta)
    return rutas


def hoja_html(piezas: list[dict], cliente: str, telefono: str, proyecto: str) -> str:
    t = totales(piezas)
    filas = "\n".join(
        "<tr>" + "".join(f"<td>{html.escape(p[c])}</td>" for c in
                         ["pieza", "cantidad", "largo", "ancho", "espesor", "color",
                          "L1", "L2", "A1", "A2", "veta", "notas"]) + "</tr>"
        for p in piezas)
    materiales = "\n".join(
        f"<li>{html.escape(m)}: {a:.2f} m²<table class='formatos'><tr><th>Tablero</th>"
        "<th>Uso del área útil</th><th>Tableros (mínimo)</th></tr>"
        + "".join(f"<tr><td>{f}</td><td>{uso:.0%}</td><td>{n}</td></tr>"
                  for f, uso, n in uso_tableros(a))
        + "</table></li>"
        for m, a in t["area"].items())
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Pedido {html.escape(proyecto)}</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 2rem; color: #222; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 0.9rem; }}
  th, td {{ border: 1px solid #999; padding: 4px 6px; text-align: left; }}
  th {{ background: #eee; }}
  .datos span {{ display: inline-block; min-width: 14rem; margin-right: 1rem; }}
  table.formatos {{ width: auto; margin: 0.3rem 0 0.8rem; }}
</style></head><body>
<h1>Pedido de corte · Madecentro Guarne</h1>
<p class="datos"><span>Cliente: {html.escape(cliente)}</span><span>Teléfono: {html.escape(telefono)}</span>
<span>Proyecto: {html.escape(proyecto)}</span><span>Fecha: {date.today():%d/%m/%Y}</span></p>
<p>Medidas en mm. Cantos: 1 = lleva tapacanto (L = lados largos, A = lados anchos).</p>
<table><thead><tr><th>Pieza</th><th>Cant.</th><th>Largo</th><th>Ancho</th><th>Esp.</th><th>Color</th>
<th>L1</th><th>L2</th><th>A1</th><th>A2</th><th>Veta</th><th>Notas</th></tr></thead>
<tbody>
{filas}
</tbody></table>
<h2>Totales</h2>
<ul>
{materiales}
<li>Tapacanto: {t["tapacanto_m"]:.2f} m</li>
</ul>
<p>El formato del tablero depende de la marca: pregúntalo al pedir. El uso se calcula sobre el área útil,
con {REFILADO} mm de refilado por eje; el número exacto de tableros lo da el optimizador.</p>
</body></html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("csv", help="lista de corte generada por la calculadora")
    parser.add_argument("--cliente", default="")
    parser.add_argument("--telefono", default="")
    parser.add_argument("--proyecto", default="")
    parser.add_argument("--madecentro", metavar="DIR",
                        help="escribe también un CSV por material para el optimizador de Madecentro")
    args = parser.parse_args()
    proyecto = args.proyecto or args.csv.rsplit("/", 1)[-1].removesuffix(".csv")
    piezas = leer_piezas(args.csv)
    sys.stdout.write(hoja_html(piezas, args.cliente, args.telefono, proyecto))
    if args.madecentro:
        for ruta in escribir_madecentro(piezas, args.madecentro, proyecto):
            print(f"Madecentro: {ruta}", file=sys.stderr)


if __name__ == "__main__":
    main()
