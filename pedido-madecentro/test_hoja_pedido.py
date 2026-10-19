import unittest
from pathlib import Path

from hoja_pedido import hoja_html, leer_piezas, pedido_madecentro, totales, uso_tableros

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
        lista = hoja.split("<h2>Totales</h2>")[0]
        self.assertEqual(lista.count("<tr><td>"), len(piezas))


class TestFormatosTablero(unittest.TestCase):
    def test_uso_por_formato_descuenta_refilado(self):
        uso = {f: (u, n) for f, u, n in uso_tableros(1.442)}
        # área útil de 2150 × 2440 con 20 mm de refilado: 2130 × 2420
        self.assertAlmostEqual(uso["2150 × 2440"][0], 1.442 / (2.130 * 2.420))
        self.assertEqual(uso["1830 × 2440"][1], 1)
        self.assertEqual(len(uso), 4)

    def test_mas_de_un_tablero(self):
        self.assertEqual(dict((f, n) for f, _, n in uso_tableros(5.0))["1830 × 2440"], 2)


class TestPedidoMadecentro(unittest.TestCase):
    def test_agrupa_por_material(self):
        pedido = pedido_madecentro(leer_piezas(NOCHERO))
        self.assertEqual(set(pedido), {"Ristretto RH 15 mm", "HDF 3 mm"})
        self.assertEqual(len(pedido["Ristretto RH 15 mm"]), 7)

    def test_cantos_largos_a_los_lados(self):
        lateral = pedido_madecentro(leer_piezas(NOCHERO))["Ristretto RH 15 mm"][0]
        # Lateral: 550 de largo (Alto) × 400 de ancho, tapacanto solo en L1
        self.assertEqual(lateral[:4], ["400", "550", "2", "Lateral"])
        self.assertEqual(lateral[5:9], ["", "", "Ristretto RH", ""])


if __name__ == "__main__":
    unittest.main()
