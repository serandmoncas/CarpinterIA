"""Convierte una lista de corte CSV en una hoja de pedido imprimible para Madecentro.

Uso: python3 pedido-madecentro/hoja_pedido.py despieces/nochero.csv --cliente "Carlos" > pedido.html
Se abre en el navegador y se imprime o se guarda como PDF.
"""

import argparse
import csv
import html
import sys
from datetime import date

AREA_TABLERO = 1.83 * 2.44  # m², tablero de 1830 × 2440


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


def hoja_html(piezas: list[dict], cliente: str, telefono: str, proyecto: str) -> str:
    t = totales(piezas)
    filas = "\n".join(
        "<tr>" + "".join(f"<td>{html.escape(p[c])}</td>" for c in
                         ["pieza", "cantidad", "largo", "ancho", "espesor", "color",
                          "L1", "L2", "A1", "A2", "veta", "notas"]) + "</tr>"
        for p in piezas)
    materiales = "\n".join(
        f"<li>{html.escape(m)}: {a:.2f} m² (≈ {a / AREA_TABLERO:.0%} de un tablero)</li>"
        for m, a in t["area"].items())
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Pedido {html.escape(proyecto)}</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 2rem; color: #222; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 0.9rem; }}
  th, td {{ border: 1px solid #999; padding: 4px 6px; text-align: left; }}
  th {{ background: #eee; }}
  .datos span {{ display: inline-block; min-width: 14rem; margin-right: 1rem; }}
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
</body></html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("csv", help="lista de corte generada por la calculadora")
    parser.add_argument("--cliente", default="")
    parser.add_argument("--telefono", default="")
    parser.add_argument("--proyecto", default="")
    args = parser.parse_args()
    proyecto = args.proyecto or args.csv.rsplit("/", 1)[-1].removesuffix(".csv")
    sys.stdout.write(hoja_html(leer_piezas(args.csv), args.cliente, args.telefono, proyecto))


if __name__ == "__main__":
    main()
