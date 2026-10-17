"""Genera la guía del curso (HTML y PDF) a partir de la plantilla y de los datos del repo.

Uso:
    python3 guia/generar_guia.py          # escribe guia/guia-del-curso.html
    python3 guia/generar_guia.py --pdf    # además exporta guia/guia-del-curso.pdf con Chrome

Las tablas de holguras y de despiece no se escriben a mano: salen de la calculadora
y de los CSV de despieces/, así la guía siempre coincide con lo que se pide a Madecentro.
"""

import argparse
import html
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "calculadora"))
sys.path.insert(0, str(RAIZ / "pedido-madecentro"))

import holguras  # noqa: E402
from hoja_pedido import leer_piezas, totales  # noqa: E402

PLANTILLA = RAIZ / "guia" / "plantilla.html"
SALIDA_HTML = RAIZ / "guia" / "guia-del-curso.html"
SALIDA_PDF = RAIZ / "guia" / "guia-del-curso.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def tabla_holguras() -> str:
    filas = "\n".join(
        f"<tr><td>{html.escape(nombre)}</td><td class='num'>{mm}</td><td>{html.escape(nota)}</td></tr>"
        for nombre, mm, nota in holguras.HOLGURAS)
    return ("<table><thead><tr><th>Dónde</th><th class='num'>mm</th><th>Cómo se usa</th></tr></thead>"
            f"<tbody>{filas}</tbody></table>")


def cantos(p: dict) -> str:
    marcas = [nombre for nombre in ("L1", "L2", "A1", "A2") if p[nombre] == "1"]
    return " ".join(marcas) if marcas else "—"


def tabla_despiece(nombre_csv: str) -> str:
    piezas = leer_piezas(str(RAIZ / "despieces" / nombre_csv))
    filas = "\n".join(
        "<tr>"
        f"<td>{html.escape(p['pieza'])}</td><td class='num'>{p['cantidad']}</td>"
        f"<td class='num'>{p['largo']}</td><td class='num'>{p['ancho']}</td>"
        f"<td>{html.escape(p['color'])} {p['espesor']}</td><td>{cantos(p)}</td>"
        f"<td>{html.escape(p['notas'])}</td>"
        "</tr>"
        for p in piezas)
    t = totales(piezas)
    resumen = " · ".join(f"{html.escape(m)}: {a:.2f} m²" for m, a in t["area"].items())
    return ("<table><thead><tr><th>Pieza</th><th class='num'>Cant.</th><th class='num'>Largo</th>"
            "<th class='num'>Ancho</th><th>Material</th><th>Tapacanto</th><th>Notas</th></tr></thead>"
            f"<tbody>{filas}</tbody></table>"
            f"<p class='pie-tabla'>Medidas en mm. {resumen} · Tapacanto: {t['tapacanto_m']:.2f} m.</p>")


def generar() -> str:
    texto = PLANTILLA.read_text(encoding="utf-8")
    reemplazos = {
        "{{tabla_holguras}}": tabla_holguras(),
        "{{despiece_caja}}": tabla_despiece("caja-herramientas.csv"),
        "{{despiece_nochero}}": tabla_despiece("nochero.csv"),
    }
    for marca, contenido in reemplazos.items():
        assert marca in texto, f"falta {marca} en la plantilla"
        texto = texto.replace(marca, contenido)
    return texto


def exportar_pdf() -> None:
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={SALIDA_PDF}", SALIDA_HTML.as_uri()],
                   check=True, capture_output=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--pdf", action="store_true", help="exportar también el PDF con Chrome")
    args = parser.parse_args()
    SALIDA_HTML.write_text(generar(), encoding="utf-8")
    print(f"HTML: {SALIDA_HTML}")
    if args.pdf:
        exportar_pdf()
        print(f"PDF:  {SALIDA_PDF}")


if __name__ == "__main__":
    main()
