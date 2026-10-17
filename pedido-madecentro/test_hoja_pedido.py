import unittest
from pathlib import Path

from hoja_pedido import hoja_html, leer_piezas, totales

NOCHERO = str(Path(__file__).parent.parent / "despieces" / "nochero.csv")


class TestTotalesNochero(unittest.TestCase):
    def test_tapacanto(self):
        # 1100 + 940 + 470 + 1782 + 1292 + 700 + 828 mm
        self.assertAlmostEqual(totales(leer_piezas(NOCHERO))["tapacanto_m"], 7.112)

    def test_area_por_material(self):
        area = totales(leer_piezas(NOCHERO))["area"]
        self.assertAlmostEqual(area["Ristretto RH 15 mm"], 1.442, places=3)
        # 546 × 496 + 444 × 350
        self.assertAlmostEqual(area["HDF 3 mm"], 0.426216, places=6)

    def test_hoja_incluye_todas_las_piezas(self):
        piezas = leer_piezas(NOCHERO)
        hoja = hoja_html(piezas, "Carlos", "", "nochero")
        self.assertEqual(hoja.count("<tr><td>"), len(piezas))


if __name__ == "__main__":
    unittest.main()
