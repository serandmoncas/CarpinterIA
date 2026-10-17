import csv
import io
import unittest
from pathlib import Path

from despiece import despiece, escribir_csv, repartir_frentes

NOCHERO = Path(__file__).parent.parent / "despieces" / "nochero.csv"
COLUMNAS_COMPARADAS = ["pieza", "cantidad", "largo", "ancho", "espesor",
                       "color", "L1", "L2", "A1", "A2"]


def filas(texto: str) -> list[dict]:
    return [{c: fila[c] for c in COLUMNAS_COMPARADAS} for fila in csv.DictReader(io.StringIO(texto))]


class TestNochero(unittest.TestCase):
    def test_frentes_del_nochero(self):
        self.assertEqual(repartir_frentes(550, 1, True), (150, 395))

    def test_reproduce_la_lista_de_referencia(self):
        salida = io.StringIO()
        escribir_csv(despiece(500, 400, 550, e=15, cajones=1, puerta="sencilla"), salida)
        self.assertEqual(filas(salida.getvalue()), filas(NOCHERO.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
