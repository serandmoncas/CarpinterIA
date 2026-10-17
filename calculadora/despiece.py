"""Genera la lista de corte de un módulo en melamina a partir de sus medidas exteriores.

Todas las medidas van en mm. Las fórmulas siguen la convención del curso: `e` es el
espesor del tablero, y la base, el techo y los entrepaños van entre los laterales.
La salida es un CSV con las columnas del pedido de Madecentro.
"""

import argparse
import csv
import sys
from dataclasses import dataclass

COLOR_MELAMINA = "Ristretto RH"
ESPESOR_HDF = 3
HOLGURA_FONDO = 2  # mm por lado del fondo de HDF
HOLGURA_FRENTE = 2  # mm por lado en frentes sobrepuestos
HOLGURA_ENTRE_PUERTAS = 3  # mm entre las dos hojas de una puerta doble
HOLGURA_ARRIBA = 1  # mm entre el techo y el frente más alto
HOLGURA_ENTRE_FRENTES = 3  # mm entre frentes de cajón y entre cajón y puerta
HOLGURA_ABAJO = 1  # mm entre la base y el frente más bajo
HOLGURA_EMBUTIDA = 1  # mm por lado en piezas que van dentro del cuerpo
HOLGURA_CORREDERA = 13  # mm por lado; confirmar con la ficha de la corredera
ALTO_FRENTE_CAJON = 150
DIFERENCIA_FRENTE_CAJA = 40  # la caja del cajón es 40 mm más baja que su frente

COLUMNAS = ["pieza", "cantidad", "largo", "ancho", "espesor", "color",
            "L1", "L2", "A1", "A2", "veta", "notas"]

UN_LARGO = (1, 0, 0, 0)
CUATRO_CANTOS = (1, 1, 1, 1)
SIN_CANTOS = (0, 0, 0, 0)


@dataclass
class Pieza:
    nombre: str
    cantidad: int
    largo: int
    ancho: int
    espesor: int
    cantos: tuple[int, int, int, int]
    notas: str = ""

    @property
    def color(self) -> str:
        return "HDF" if self.espesor == ESPESOR_HDF else COLOR_MELAMINA

    def fila(self) -> dict:
        l1, l2, a1, a2 = self.cantos
        return {"pieza": self.nombre, "cantidad": self.cantidad, "largo": self.largo,
                "ancho": self.ancho, "espesor": self.espesor, "color": self.color,
                "L1": l1, "L2": l2, "A1": a1, "A2": a2, "veta": "", "notas": self.notas}


def repartir_frentes(alto: int, cajones: int, con_puerta: bool) -> tuple[int, int | None]:
    """Devuelve (alto de cada frente de cajón, alto de la puerta o None).

    Los frentes son sobrepuestos y cubren el alto del módulo, dejando holguras
    arriba, abajo y entre frentes. Para el nochero (alto 550, 1 cajón, con puerta)
    el resultado debe ser (150, 395).
    """
    disponible = alto - HOLGURA_ARRIBA - HOLGURA_ABAJO
    if not con_puerta:
        if not cajones:
            return 0, None
        return (disponible - (cajones - 1) * HOLGURA_ENTRE_FRENTES) // cajones, None
    alto_puerta = disponible - cajones * (ALTO_FRENTE_CAJON + HOLGURA_ENTRE_FRENTES)
    return (ALTO_FRENTE_CAJON if cajones else 0), alto_puerta


def despiece(ancho: int, fondo: int, alto: int, e: int = 15, cajones: int = 0,
             puerta: str = "sencilla", corredera: int = 350) -> list[Pieza]:
    ancho_interior = ancho - 2 * e
    ancho_frente = ancho - 2 * HOLGURA_FRENTE
    piezas = [
        Pieza("Lateral", 2, alto, fondo, e, UN_LARGO),
        Pieza("Base y techo", 2, ancho_interior, fondo, e, UN_LARGO),
    ]
    if cajones and puerta != "ninguna":
        piezas.append(Pieza("Entrepaño fijo", 1, ancho_interior, fondo, e, UN_LARGO))
    piezas.append(Pieza("Fondo", 1, alto - 2 * HOLGURA_FONDO, ancho_frente,
                        ESPESOR_HDF, SIN_CANTOS))

    alto_frente_cajon, alto_puerta = repartir_frentes(alto, cajones, puerta != "ninguna")
    if puerta == "sencilla":
        piezas.append(Pieza("Puerta", 1, ancho_frente, alto_puerta, e, CUATRO_CANTOS))
    elif puerta == "doble":
        ancho_hoja = (ancho_frente - HOLGURA_ENTRE_PUERTAS) // 2
        piezas.append(Pieza("Puerta", 2, ancho_hoja, alto_puerta, e, CUATRO_CANTOS))

    if cajones:
        ancho_caja = ancho_interior - 2 * HOLGURA_CORREDERA
        alto_caja = alto_frente_cajon - DIFERENCIA_FRENTE_CAJA
        piezas += [
            Pieza("Frente de cajón", cajones, ancho_frente, alto_frente_cajon, e, CUATRO_CANTOS),
            Pieza("Costado de cajón", 2 * cajones, corredera, alto_caja, e, UN_LARGO),
            Pieza("Frente interior y trasera de cajón", 2 * cajones,
                  ancho_caja - 2 * e, alto_caja, e, UN_LARGO),
            Pieza("Fondo de cajón", cajones, ancho_caja, corredera, ESPESOR_HDF, SIN_CANTOS),
        ]
    return piezas


def escribir_csv(piezas: list[Pieza], salida) -> None:
    escritor = csv.DictWriter(salida, fieldnames=COLUMNAS)
    escritor.writeheader()
    for pieza in piezas:
        escritor.writerow(pieza.fila())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ancho", type=int, required=True)
    parser.add_argument("--fondo", type=int, required=True)
    parser.add_argument("--alto", type=int, required=True)
    parser.add_argument("--e", type=int, default=15, help="espesor del tablero")
    parser.add_argument("--cajones", type=int, default=0)
    parser.add_argument("--puerta", choices=["ninguna", "sencilla", "doble"], default="sencilla")
    parser.add_argument("--corredera", type=int, default=350, help="largo de la corredera")
    args = parser.parse_args()
    escribir_csv(despiece(args.ancho, args.fondo, args.alto, args.e, args.cajones,
                          args.puerta, args.corredera), sys.stdout)


if __name__ == "__main__":
    main()
