"""Genera la página de holguras del curso a partir de las constantes de la calculadora.

Uso: python3 calculadora/holguras.py > material/holguras.html
Así la página impresa y los despieces usan siempre los mismos números.
"""

import sys

import despiece as d

HOLGURAS = [
    ("Frente sobrepuesto, a cada lado", d.HOLGURA_FRENTE,
     "La puerta o el frente queda 2 × esta medida más angosto que el mueble."),
    ("Entre frentes", d.HOLGURA_ENTRE_FRENTES,
     "Entre dos cajones, y entre el cajón y la puerta."),
    ("Entre las dos hojas de una puerta doble", d.HOLGURA_ENTRE_PUERTAS, ""),
    ("Arriba del frente más alto", d.HOLGURA_ARRIBA, ""),
    ("Abajo del frente más bajo", d.HOLGURA_ABAJO, ""),
    ("Corredera telescópica, a cada lado", d.HOLGURA_CORREDERA,
     "Caja del cajón = ancho interior − 2 × esta medida. Confirmar con la ficha de la corredera."),
    ("Fondo de HDF, a cada lado", d.HOLGURA_FONDO, "El fondo queda 2 × esta medida más pequeño que el mueble."),
    ("Pieza embutida, a cada lado", d.HOLGURA_EMBUTIDA,
     "Entrepaños móviles y piezas que entran entre los laterales sin ir fijas."),
]


def pagina() -> str:
    filas = "\n".join(f"<tr><td>{nombre}</td><td>{mm}</td><td>{nota}</td></tr>"
                      for nombre, mm, nota in HOLGURAS)
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Holguras</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 2rem; color: #222; max-width: 50rem; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ border: 1px solid #999; padding: 6px 8px; text-align: left; vertical-align: top; }}
  th {{ background: #eee; }}
  td:nth-child(2) {{ text-align: right; font-weight: bold; white-space: nowrap; }}
</style></head><body>
<h1>Holguras</h1>
<p>La holgura es el espacio que se deja para que una pieza abra, corra o entre sin rozar.
Medidas en mm, para melamina de 15 mm. Ejemplo con el nochero de 500 mm de ancho:
puerta de 500 − 2 × {d.HOLGURA_FRENTE} = {500 - 2 * d.HOLGURA_FRENTE} mm; caja del cajón de
470 − 2 × {d.HOLGURA_CORREDERA} = {470 - 2 * d.HOLGURA_CORREDERA} mm.</p>
<table><thead><tr><th>Dónde</th><th>mm</th><th>Cómo se usa</th></tr></thead>
<tbody>
{filas}
</tbody></table>
</body></html>
"""


if __name__ == "__main__":
    sys.stdout.write(pagina())
