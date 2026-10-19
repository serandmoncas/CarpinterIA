# Biblioteca de CarpinterIA

Guías, planos, fichas técnicas y herramientas de referencia para el curso de carpintería en melamina. Búsqueda hecha en octubre de 2026.

Los PDF son de sus fabricantes o autores. Se descargaron de sus sitios oficiales, donde se distribuyen gratis, pero no tienen licencia libre. Por eso **no se suben al repo**, que es público: quedan solo en el computador (ver `.gitignore`), y aquí está el link original de cada uno. Para recuperar un archivo, se baja de nuevo desde su link.

## Lo más útil para el curso

- **El tablero no siempre mide lo mismo.**
  - Pelikano, el que más vende Madecentro, mide 2150 × 2440 mm.
  - Arauco VESTO de 15 mm viene en 1830 × 2500 o en 2150 × 2440 mm. El RH solo viene en 2150 × 2440.
  - Antes de optimizar un despiece hay que preguntar la marca y el formato.
- **Madecentro corta con estos parámetros:** su optimizador usa por defecto una sierra (kerf) de 5 mm, un refilado de 20 mm por eje y un retazo mínimo de 100 × 100 mm.
  - Su plantilla pide estas columnas: Ancho, Alto, Cantidad, Descripción, Veta (Horizontal o Vertical), Canto Superior, Inferior, Izquierdo y Derecho (con el color del canto) y Servicios.
  - El tablero se escoge una sola vez para toda la optimización.
- **La holgura de las correderas está confirmada.** Para la corredera de bolas de 12,7 mm, Häfele indica de 12,9 a 13,2 mm por lado y Arauco de 12,5 a 13 mm. El riel va a unos 2 mm del frente del costado.
- **Cazoleta de 35 mm:**
  - El borde del agujero queda a 3–7 mm del canto de la puerta (Arauco simplifica en 4 mm, así que el centro queda a unos 21,5 mm). La profundidad es de 11,5 a 13 mm y el frente debe tener mínimo 13 mm.
  - Cantidad de bisagras según el alto de la puerta: hasta 0,9 m lleva 2, hasta 1,6 m lleva 3, hasta 2,0 m lleva 4 y hasta 2,4 m lleva 5. Van a 7,5–10 cm de los extremos.
- **Tornillos:**
  - El autorroscante va a mínimo 25 mm del borde y a 50 mm de las esquinas, con broca guía de 3 mm para el de 4 mm. Coincide con lo que enseña el curso.
  - El canto agarra el tornillo menos que la cara: en MDP de 15 mm, más de 600 N contra más de 800 N.
- **Cocina:**
  - Módulos bajos: mesón a 90 cm, 58 cm de fondo de costado y zócalo de 10 a 15 cm.
  - Módulos altos: de 30 a 35 cm de fondo, colgados a 1,40–1,50 m.
  - Anchos de módulo: 30, 45, 50, 60, 75, 80, 90 y 100 cm.

## Melamina y tableros (`melamina/`)

| Recurso | Fuente | Idioma | Por qué sirve | Archivo |
|---|---|---|---|---|
| [Ficha técnica Melamina VESTO Colombia 2022](https://arauco.com/colombia/wp-content/uploads/sites/18/2022/05/5426_COLOMBIA_FICHA_TECNICA_MELAMINA_VESTO_2022.pdf) | Arauco Colombia | ES | Medidas del tablero, retención de tornillo en cara y canto, corte, tapacanto y almacenamiento | `arauco-colombia-ficha-tecnica-melamina-vesto.pdf` |
| [Cómo unir tableros con tornillos autorroscantes](https://arauco.com/chile/wp-content/uploads/sites/14/2019/03/12_15955_foll_web_muebleria_unir-autorroscante_chile_28_sep_2015_963.pdf) | Arauco Chile | ES | Tabla de espesor, tornillo y broca guía, y distancias al borde y a las esquinas | `arauco-como-unir-con-autorroscantes.pdf` |
| [Cómo unir tableros con tornillos soberbios](https://arauco.com/chile/wp-content/uploads/sites/14/2019/03/03_15955_foll_web_muebleria_unir_tableros_chile_28_sep_2015_1053.pdf) | Arauco Chile | ES | Unión tipo confirmat: broca escalonada, avellanado y perforación centrada | `arauco-como-unir-tableros-tornillos-soberbios.pdf` |
| [Isla de cocina (Serie Cómo Hacer)](https://arauco.com/chile/wp-content/uploads/sites/14/2020/10/3599_pap_sch_isla_de_cocina_chile_23sep_20visual-pdf_503_so1-2.pdf) | Arauco Chile | ES | Mueble de cocina con zócalo. El despiece marca qué cantos llevan tapacanto | `arauco-como-hacer-isla-de-cocina.pdf` |
| [Elementos para la fabricación de muebles con tableros de melamina](https://cdn.www.gob.pe/uploads/document/file/571557/1._Elementos_para_la_fabricaci%C3%B3n_de_muebles_de_Melamina.pdf) | CITEmadera (Perú, entidad pública) | ES | El manual más completo para principiantes: tableros, tapacantos, pegantes, tornillos, sistema 32, minifix y seguridad | `citemadera-elementos-fabricacion-muebles-melamina.pdf` |
| [Mejora de procesos de carpintería en madera](https://cdn.www.gob.pe/uploads/document/file/571604/05._Carpinteria.pdf) | CITEmadera | ES | Carpintería y ebanistería en general: habilitado, maquinado y ensamble | `citemadera-mejora-procesos-carpinteria-madera.pdf` |
| [Catálogo de cantos Madecentro](https://issuu.com/madecentrocolombiasas/docs/catalogo_cantos_madecentro) | Madecentro | ES | Los tapacantos que venden donde se manda a cortar | solo link (Issuu) |
| [Catálogo de tableros Pelikano 2024-2026](https://issuu.com/madecentrocolombiasas/docs/cat_logo_tableros_pel_kano_2024-2026) | Madecentro / Pelikano | ES | Diseños y versiones estándar y RH | solo link (Issuu) |
| [RAUKANTEX PVC, información técnica](https://www.rehau.com/downloads/327058/raukantex-pvc.pdf) | REHAU | ES | Propiedades del tapacanto de PVC | solo link (sin revisar: el servidor bloqueó la descarga) |

## Herrajes y sistema 32 (`herrajes/`)

| Recurso | Fuente | Idioma | Por qué sirve | Archivo |
|---|---|---|---|---|
| [Cómo instalar bisagras de parche](https://arauco.com/colombia/wp-content/uploads/sites/18/2020/10/05_15955_foll_web_muebleria_bisagras_arco_02_sep_15_1703.pdf) | Arauco Colombia | ES | Tipos de brazo, cuántas bisagras lleva cada puerta, cotas de perforación y ajuste | `arauco-como-instalar-bisagras-cazoleta.pdf` |
| [Cómo instalar correderas](https://arauco.com/chile/wp-content/uploads/sites/14/2019/03/09_pap_correderas_chile_30jul_2015_992.pdf) | Arauco Chile | ES | Corredera estándar y telescópica, holgura y montaje | `arauco-como-instalar-correderas.pdf` |
| [CLIP top BLUMOTION 105°, hoja técnica](https://d2.blum.com/services/BEC003/cme101332_td_dok_bau_$ses_$aof_$v1.pdf) | Blum | ES | Tablas de recubrimiento para escoger entre recta, curva y supercurva, distancia de la cazoleta y ajuste 3D | `blum-clip-top-blumotion-105-hoja-tecnica.pdf` |
| [Sensys, hojas de montaje](https://media.hornbach.nl/hb/installationmanual/as.80877187.pdf) ([2](https://media.hornbach.nl/hb/installationmanual/as.80877036.pdf), [3](https://media.hornbach.nl/hb/installationmanual/as.80877493.pdf)) | Hettich | Gráfico, multilingüe | Montaje solapado, central e interior, y bisagras según el alto de la puerta | `hettich-sensys-montaje-solapada-central-interior.pdf` |
| [Bisagras de cazoleta, guía de instalación (pp. 9.12–9.15)](https://files.hafele.co.uk/CatalogFiles/www/23T9-12.pdf) | Häfele UK | EN | Cazoleta, patrón 45/9,5, juego mínimo y rangos de ajuste | `hafele-bisagras-cazoleta-guia-instalacion.pdf` |
| [Grass Tiomos y Nexis (pp. 9.45–9.47)](https://files.hafele.co.uk/CatalogFiles/www/23T9-45.pdf) | Häfele UK | EN | Patrones de perforación de 45 y 48 mm y tabla de recubrimiento | `grass-bisagras-cazoleta-guia-instalacion.pdf` |
| [Accuride 3832, instalación](https://hs-europe.accuride.com/hubfs/InstallationGuides/3832.pdf) | Accuride | Multilingüe con ES | Corredera telescópica de bolas típica: largos y montaje | `accuride-3832-corredera-telescopica-instalacion.pdf` |
| [Accuride 3832 en el catálogo Häfele (p. 10.223)](https://files.hafele.co.uk/CatalogFiles/www/18T10-223.PDF) | Häfele UK | EN | Regla oficial de la holgura lateral | `hafele-accuride-3832-holgura-lateral.pdf` |
| [Minifix 15 (pp. 7.11 y 7.13)](https://files.hafele.co.uk/CatalogFiles/www/23T7-11.pdf) | Häfele UK | EN | Cómo funciona la excéntrica y profundidad de perforación | `hafele-minifix-15-sistema-y-perforacion.pdf` |
| [Confirmat (pp. 13.36–13.37)](https://files.hafele.co.uk/CatalogFiles/www/23T13-36.pdf) | Häfele UK | EN | Esquema de taladrado del confirmat 7×50 | `hafele-confirmat-perforacion.pdf` |
| [Plantillas del sistema 32 (pp. 7.50–7.53)](https://files.hafele.co.uk/CatalogFiles/www/23T7-50.pdf) | Häfele UK | EN | Filas de agujeros de Ø5 cada 32 mm a 37 mm del borde, con plantilla | `hafele-sistema-32-plantillas-perforacion.pdf` |
| [Soportes de entrepaño de 5 mm (pp. 7.173–7.174)](https://files.hafele.co.uk/CatalogFiles/www/23T7-173.pdf) | Häfele UK | EN | Pines de soporte y su carga | `hafele-soportes-entrepano-5mm.pdf` |
| [Colgadores Traser (pp. 7.214–7.215)](https://files.hafele.co.uk/CatalogFiles/www/23T7-214.pdf) | Häfele UK | EN | Anclaje a la pared de muebles altos de cocina y baño | `hafele-colgadores-muebles-altos-pared.pdf` |
| [Patas niveladoras (pp. 11.56–11.58)](https://files.hafele.co.uk/CatalogFiles/www/23T11-56.pdf) | Häfele UK | EN | Patas y zócalo para módulos bajos | `hafele-patas-niveladoras-zocalo.pdf` |
| [Cómo instalar correderas paso a paso](https://www.homecenter.com.co/homecenter-co/guias-de-compra/aprenda-como-instalar-correderas-paso-a-paso) | Homecenter Colombia | ES | Guía local con productos que se consiguen aquí | solo link |

Los PDF de Häfele que cubren varias páginas se armaron juntando las páginas oficiales sueltas del catálogo. Cada link lleva a la primera página.

## Planos de muebles (`planos/`)

| Recurso | Mueble | Fuente | Por qué sirve | Archivo |
|---|---|---|---|---|
| [Kit muebles para baño](https://arauco.com/peru/wp-content/uploads/sites/22/2021/03/3471_pdf_web_pap_sch_kit_ban-o_chile_29jul_20-pdf_496_so2.pdf) | Baño | Arauco | **En 15 mm**, 1 tablero, con lista de piezas, tapacanto y esquema de corte. Es el más parecido al curso | `arauco-kit-muebles-bano.pdf` |
| [Home Office](https://arauco.com/colombia/wp-content/uploads/sites/18/2020/10/3-home-office-serie-como-hacer-hc-pdf_501_so1.pdf) | Escritorio | Arauco Colombia | **En 15 mm**, con la posición de cada tornillo y el anclaje a muro | `arauco-mini-oficina-home-office.pdf` |
| [Estante modular](https://arauco.com/chile/wp-content/uploads/sites/14/2019/03/02_15955_foll_web_muebleria_estante_modular_chile_28_sep_2015_1063.pdf) | Biblioteca | Arauco Chile | **En 15 mm**, cubos de 40 cm: un buen primer proyecto | `arauco-estante-modular-biblioteca.pdf` |
| [Cómo diseñar y construir una cocina](https://arauco.com/peru/wp-content/uploads/sites/22/2020/10/3228_pdf_web_sch_peru_folleto_como_disenar_construir_cocina_peru_15jun_20-pdf_377_so2.pdf) | Cocina | Arauco Perú | Módulo bajo, alto y torre, con medidas estándar | `arauco-como-disenar-construir-cocina.pdf` |
| [Cocina Arancibia](https://arauco.com/peru/wp-content/uploads/sites/22/2020/10/folleto-pdf_392_so2.pdf) | Cocina | Arauco | Lista de cortes de módulos altos. La base es de listones de pino, no de tablero | `arauco-cocina-arancibia-modulos.pdf` |
| [Armario móvil](https://arauco.com/chile/wp-content/uploads/sites/14/2021/09/4729_PDF_WEB_SCH_PAP_ARMARIO_MOVIL_CHILE_22Sep_21_E02.pdf) | Closet | Arauco Chile | Barra, repisas y ruedas. Está en 18 mm: hay que ajustarlo a 15 | `arauco-armario-movil-closet.pdf` |
| [Vin-A](https://arauco.com/peru/wp-content/uploads/sites/22/2022/05/5178_PDF_WEB_PAP_SCH_VIN-A_PERU_17May_22.pdf) | Habitación y nochero | Arauco Perú | Velador con cajón y correderas, cabecera y base de cama. En 18 mm | `arauco-vin-a-velador-dormitorio.pdf` |
| [Mueble para TV Boho](https://arauco.com/peru/wp-content/uploads/sites/22/2021/03/3871_PDF_WEB_PAP_SCH_MUEBLE_PARA_TV_BOHO_PROY_03_PERU_15Feb_21.pdf) | Sala | Arauco Perú | Mueble colgado a muro con bisagras de 35 mm. En 18 mm | `arauco-mueble-tv-boho.pdf` |
| [Cálida Bienvenida](https://arauco.com/peru/wp-content/uploads/sites/22/2022/05/5210_PDF_WEB_PAP_SCH_CALIDA_BIENVENIDA_PERU_17May_22.pdf) | Zapatero | Arauco Perú | Zapatero con banca y perchero. En 18 mm | `arauco-mueble-entrada-zapatero.pdf` |
| [Pequeña caja de herramientas](https://corporate.homedepot.com/document/4329) | Caja de herramientas | The Home Depot | Forma clásica de la caja abierta con cabeceras en punta. Sin medidas | `homedepot-caja-herramientas-ninos.pdf` |
| [Wood Toolbox Plans](https://ana-white.com/woodworking-projects/wood-toolbox-plans) | Caja de herramientas | Ana White | Plan para principiantes con lista de corte, en pulgadas | solo link |
| [36" Sink Base Kitchen Cabinet](https://www.ana-white.com/2014/01/plans/36-sink-base-kitchen-cabinet-momplex-vanilla-kitchen) | Cocina | Ana White | Módulo bajo de lavaplatos, en contrachapado y pulgadas | solo link |
| [Cuadro normativo DS 49](https://www.minvu.gob.cl/wp-content/uploads/2022/10/Cuadro-Normativo-Abreviado-Llamado-Cooperativas-2022.pdf) | Medidas mínimas | MINVU Chile | Medidas oficiales de closet (100 × 60 × 140 cm mínimo por dormitorio), cocina y baño | `minvu-cuadro-normativo-mobiliario-vivienda.pdf` |
| [Closet Rod Height](https://www.bobvila.com/articles/closet-rod-height/) | Closet | Bob Vila | Altura de la barra: unos 168 cm si es sencilla; 208 y 103 cm si es doble | solo link |

## Despiece y optimización de corte (`despiece/`)

| Recurso | Tipo | Gratis | Mac o web | Por qué sirve | Archivo |
|---|---|---|---|---|---|
| [Optimizador de Madecentro](https://tablerosmadecentro.com/) | Software | Sí, con cuenta | Web | Es la herramienta oficial del lugar donde se manda a cortar: arma el plano de corte y cotiza en pesos | solo link |
| [Diseño y desarrollo de muebles con tableros de melamina](https://cdn.www.gob.pe/uploads/document/file/571560/2._Dise%C3%B1o_y_Desarrollo_de_Muebes_con_melamina.pdf) | Guía | Sí | PDF | Plano constructivo, despiece, lista de piezas con tapacanto y optimización (80 págs.) | `citemadera-diseno-desarrollo-muebles-melamina.pdf` |
| [Mueble auxiliar Handwoven](https://arauco.com/peru/wp-content/uploads/sites/22/2022/05/5211_PDF_WEB_PAP_SCH_HANDWOVEN_PERU_17May_22.pdf) | Ejemplo de despiece | Sí | PDF | Lista de corte profesional con tapacanto por lado y esquemas de corte por color | `arauco-proyecto-mueble-auxiliar-handwoven-despiece.pdf` |
| [Optimizar una placa de melamina](https://unlp.edu.ar/wp-content/uploads/2026/03/Optimizar-una-placa-de-melamina.pdf) | Guía | Sí | PDF | En 4 páginas: kerf, refilado, veta y rendimiento (más de 85 % es bueno). Informal, sin autor | `unlp-optimizar-placa-melamina.pdf` |
| [Optimizador Servidos](https://servidos.ar/optimizador-corte-placas) | Software | Sí, sin registro | Web | Explica bien el kerf y el refilado. Sirve para practicar en clase | solo link |
| [OpenCutList](https://docs.opencutlist.org/) | Software | Libre (GPL-3.0) | Mac, con SketchUp de escritorio | Lista de piezas, diagramas de corte y tapacanto. No funciona con SketchUp Free | solo link |
| [SketchUp Free](https://app.sketchup.com/) | Software | Sí, uso personal | Web | Modelado 3D. No admite extensiones | solo link |
| [FreeCAD + Woodworking](https://github.com/dprojects/Woodworking) | Software | Libre | Mac | Lista de corte automática. Cuesta aprenderlo | solo link |
| [OptiCutter](https://www.opticutter.com/) | Software | Plan gratis limitado | Web | Optimizador en español | solo link |
| [CutList Optimizer](https://www.cutlistoptimizer.com/) | Software | Gratis limitado | Web | Kerf, veta y cantos, y exporta a PDF | solo link |
| [Tutorial de MaxCut](https://www.paoson.com/blog/es/como-utilizar-el-optimizador-maxcut-n35/) | Guía | Edición gratis | Solo Windows | El optimizador más común en talleres | solo link |

## No se consiguió de forma legítima

- Fichas de Masisa (los links dan 404) y de Tablemac/Duratex (no hay fichas públicas).
- Guías de Egger y REHAU: sus servidores bloquean la descarga.
- Una hoja de fabricante para antivuelco o barra de closet.
- Libros con licencia libre en español.
