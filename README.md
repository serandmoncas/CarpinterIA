# CarpinterIA

Material y herramientas para el **curso de carpintería en melamina**. Son 4 sesiones en las que cada participante diseña su mueble modular, lo manda a cortar en Madecentro Guarne y lo arma.

- `HANDOFF.md`: estado del proyecto, decisiones tomadas y pendientes.
- `despieces/`: listas de corte de referencia en CSV, en 15 mm.
- `calculadora/`: genera despieces a partir de las medidas exteriores.
- `pedido-madecentro/`: plantilla de pedido.
- `ebooks/`: fuentes y versiones corregidas del pack de ebooks.
- `fotos/`: fotos del closet y del piloto.

## Calculadora

```sh
python3 calculadora/despiece.py --ancho 500 --fondo 400 --alto 550 --cajones 1 --puerta sencilla
python3 -m unittest discover calculadora
```
