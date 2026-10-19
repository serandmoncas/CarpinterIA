# CarpinterIA

Material y herramientas para el **curso de carpintería en melamina**. Son 4 sesiones en las que cada participante diseña su mueble modular, lo manda a cortar en Madecentro Guarne y lo arma.

- `HANDOFF.md`: estado del proyecto, decisiones tomadas y pendientes.
- `despieces/`: listas de corte de referencia en CSV, en 15 mm.
- `calculadora/`: genera despieces a partir de las medidas exteriores.
- `pedido-madecentro/`: plantilla de pedido.
- `material/`: páginas imprimibles para el curso. `holguras.html` se genera con `python3 calculadora/holguras.py > material/holguras.html`.
- `piloto/`: hoja para cronometrar el piloto y encuesta final.
- `guia/`: guía del curso para los estudiantes, en HTML y PDF. El texto está en `guia/plantilla.html`; las tablas de holguras y despieces se llenan desde la calculadora con `python3 guia/generar_guia.py --pdf`.
- `ebooks/`: fuentes y versiones corregidas del pack de ebooks.
- `biblioteca/`: guías, planos, fichas de herrajes y herramientas de despiece de terceros. En git va solo el índice (`biblioteca/README.md`) con los links; los PDF quedan en local.
- `fotos/`: fotos del closet y del piloto.

## Calculadora

```sh
python3 calculadora/despiece.py --ancho 500 --fondo 400 --alto 550 --cajones 1 --puerta sencilla
python3 -m unittest discover calculadora
```

## Hoja de pedido

```sh
python3 pedido-madecentro/hoja_pedido.py despieces/nochero.csv --cliente "Carlos" > pedido.html
```

Se abre en el navegador y se imprime o se guarda como PDF. Incluye el área por material y los metros de tapacanto, que sirven para cotizar, y cuántos tableros se usan en cada formato (1830 × 2440, 2150 × 2440, 1830 × 2500 y 2070 × 2800), descontando 20 mm de refilado.

Para el optimizador de Madecentro (tablerosmadecentro.com), agrega `--madecentro pedidos/`: escribe un CSV por material con sus columnas (Ancho, Alto, Cantidad, Descripción, Veta, cantos y Servicios), listo para abrir en Excel.
