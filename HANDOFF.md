# Handoff: Curso de Carpintería en Melamina

Actualizado: 17 oct 2026 · Dueño: Sergio Monsalve (Yolombal, Guarne)

## Objetivo

Montar un curso **vendible** de carpintería en melamina: 4 sesiones de unas 4 h, una cada 15 días. Cada participante diseña, manda a cortar en Madecentro Guarne y arma su propio mueble modular, que se lleva a casa. El piloto es con Carlos y Diana el fin de semana del 24–25 oct 2026.

## Documentos existentes (Claude Docs)

| Doc | URL | Contenido |
| --- | --- | --- |
| Curso de Carpintería en Melamina | https://claude.ai/code/artifact/ebb78c5c-7583-44e8-a70c-fd3ad4261c16 | Plan de las 4 sesiones, logística, precio, checklist del piloto |
| Revisión del pack de melamina | https://claude.ai/code/artifact/057b3ce9-f896-4c65-bbf5-7ca2eb3672bc | Errores de los 5 ebooks, vocabulario para Colombia, nochero corregido, cómo encaja el pack en el curso |

## Decisiones tomadas

- **Material:** melamina Kronospan Ristretto RH de **15 mm**, de Madecentro. Fondos en HDF de 3 mm. Todas las fórmulas se escriben con `e` (por ejemplo, ancho interior = ancho − 2e).
- **Corte:** lo hace Madecentro, con tapacanto incluido. En el taller solo se perfora, se ensambla y se ponen los herrajes.
- **Proyecto del curso:** un nochero de 500 × 400 × 550 mm con una puerta y un cajón. Ambos frentes son sobrepuestos.
- **Uniones:** confirmat de 7 × 50. Bisagras de cazoleta de 35 mm rectas. Correderas telescópicas de 350 mm.
- **Lenguaje:** español de Colombia. El voseo se puede usar, pero de forma consistente.
- **Ubicación del pack de ebooks:** de los 5 ebooks, 4 sirven de apoyo a las sesiones. El de negocio queda como bono o como segundo nivel.

## Pack de ebooks (fuente)

Son 5 PDFs de infografías generadas con IA. Cada página es una imagen, así que el texto no se puede editar en el PDF. Para corregirlos hay que regenerar las páginas o rehacerlas desde la fuente.

| Abrev. | Título | Sesión |
| --- | --- | --- |
| MC | Melamina desde cero | 1 y 3 |
| MD | Medición, despiece y optimización | 2 |
| MB | Muebles básicos paso a paso | 1, 3 y 4 |
| CC | Cocinas y closets a medida | 2 y 4 |
| NM | Negocio de muebles en melamina | después del curso |

> Pendiente: ubicar los archivos fuente (los prompts o el diseño original) de cada ebook y ponerlos en `ebooks/fuente/`.

## Lista de corte de referencia: nochero en 15 mm

Medidas en mm. Tablero de 1830 × 2440. El nochero usa aproximadamente 1/3 del tablero.

| Pieza | Cant. | Largo | Ancho | Material | Tapacanto |
| --- | --- | --- | --- | --- | --- |
| Lateral | 2 | 550 | 400 | Melamina 15 | 1 largo |
| Base y techo | 2 | 470 | 400 | Melamina 15 | 1 largo |
| Entrepaño fijo (cara superior a 405) | 1 | 470 | 400 | Melamina 15 | 1 largo |
| Fondo | 1 | 546 | 496 | HDF 3 | — |
| Puerta | 1 | 496 | 395 | Melamina 15 | 4 cantos |
| Frente de cajón | 1 | 496 | 150 | Melamina 15 | 4 cantos |
| Costado de cajón | 2 | 350 | 110 | Melamina 15 | 1 largo |
| Frente interior y trasera de cajón | 2 | 414 | 110 | Melamina 15 | 1 largo |
| Fondo de cajón | 1 | 444 | 350 | HDF 3 | — |

Holgura de la corredera: unos 13 mm por lado (470 − 26 = 444). **Hay que confirmarla con la ficha de la corredera que se compre.**

## Pendientes (en orden)

### Antes del piloto (24–25 oct)
- [ ] Confirmar el día con Carlos y escribirle a Diana para que escoja su proyecto de práctica (caja de herramientas, nochero o cajón).
- [ ] Comprar prensas (4 de 30 cm o más por pareja) y gafas extra.
- [ ] Pedir la melamina del closet en Madecentro (está pendiente de que entre la plata).
- [ ] Cronometrar cada bloque del piloto y hacer una encuesta al final.

### Material del curso
- [ ] Rehacer en 15 mm, con medidas que cuadren, los despieces de MB: cómoda, zapatero, escritorio, estantería y "cómo leer".
- [ ] Rehacer en MD: la página de descontar espesor (el ejemplo está al revés), el despiece a escala, la optimización 2 (incluir kerf y refilado) y la lista de corte de ejemplo.
- [ ] Crear la hoja de pedido para Madecentro (CSV y PDF) con las columnas: pieza, cantidad, largo, ancho, espesor, color, cantos (L1 L2 A1 A2), veta y notas.
- [ ] Crear una página de holguras: 1–3 mm en puertas, unos 13 mm por lado en correderas, 1 mm en piezas embutidas.
- [ ] Agregar el confirmat y el sistema 32 a MC.
- [ ] Aplicar el vocabulario de Colombia y corregir la ortografía. La tabla completa está en el doc de revisión.
- [ ] Corregir la seguridad: no usar guantes con herramientas que giran, y agregar el anclaje del módulo de closet de 2 m.
- [ ] Reemplazar las imágenes generadas por fotos reales del closet y del piloto.
- [ ] En NM, agregar una cotización de ejemplo en pesos, RUT y facturación electrónica, y la garantía según la Ley 1480 de 2011.

### Negocio
- [ ] Pedir a Madecentro el precio del kit del nochero (corte y tapacanto).
- [ ] Definir si el material va incluido en el precio y cuál es el cupo (4–6 personas).
- [ ] Proponer a Madecentro un descuento para los alumnos y una charla en el punto de Guarne.

## Estructura de carpetas

```
CarpinterIA/
├── HANDOFF.md
├── despieces/          # una lista de corte CSV por proyecto, en 15 mm
│   └── nochero.csv
├── calculadora/        # script que genera despieces a partir de las medidas exteriores y e
├── pedido-madecentro/  # plantilla de pedido
├── ebooks/
│   ├── fuente/
│   └── corregidos/
└── fotos/              # fotos del closet y del piloto
```

## Primera tarea sugerida en la terminal

Escribir `calculadora/despiece.py`. Recibe ancho, fondo, alto, `e`, número de cajones y tipo de puerta, y devuelve la lista de corte en CSV con el formato de Madecentro. La prueba es que reproduzca exactamente la tabla del nochero de arriba. Con esa herramienta se pueden regenerar sin errores todos los despieces del pack.
