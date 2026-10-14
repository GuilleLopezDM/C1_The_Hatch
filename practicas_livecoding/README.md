# Prácticas de livecoding

Ocho notebooks independientes: cuatro basados en viviendas y cuatro en energía.
Cada práctica incluye los datos preparados, una consigna concreta, una función para
completar, pruebas con resultados esperados, ejecución con datos reales y una pista opcional.

## Empezar

1. Abrí una práctica de la tabla y seleccioná el kernel de `.venv` del proyecto.
2. Ejecutá las celdas de **Preparación lista**.
3. En **Tu función**, reemplazá `raise NotImplementedError(...)` por tu código.
4. Ejecutá esa celda y después **Pruebas y ejecución real**.
5. Si aparece `OK`, revisá la salida guardada en la variable `resultado`.

También podés usar **Ejecutar todo**. Mientras no hayas completado la función,
las pruebas muestran `PENDIENTE`. Después de cambiar tu código, siempre ejecutá
primero la celda que define la función y después la de pruebas.

No hace falta ejecutar los notebooks de análisis. Cada práctica carga sus datos desde cero.
Tiempo sugerido: 20–30 minutos por ejercicio. Explicá tus decisiones en voz alta mientras programás.

## Viviendas

| Práctica | Función a completar | Qué practicás |
|---|---|---|
| [01 · Extremos por costa](viviendas/01_extremos_por_costa.ipynb) | `extraer_extremos_por_costa` | Mediana por `ocean_proximity`, distancia absoluta y extracción de las cinco filas más alejadas |
| [02 · Resumen por costa](viviendas/02_resumen_por_costa.ipynb) | `resumir_por_costa` | Filtrar un intervalo de ingreso y calcular conteos y medianas por grupo |
| [03 · Filtro por percentiles](viviendas/03_filtro_por_percentiles.ipynb) | `curar_viviendas` | Combinar condiciones sobre tres ratios y excluir el precio máximo |
| [04 · Sensibilidad a la imputación](viviendas/04_sensibilidad_imputacion.ipynb) | `comparar_correlaciones` | Comparar Pearson con y sin filas imputadas |

La primera retoma tu livecoding anterior: la mediana corresponde a `median_house_value`
dentro de cada categoría de costa. Se extraen las **filas completas**, con su índice original.
Las distancias son absolutas, por lo que pueden aparecer precios por encima o por debajo de la mediana.

## Energía

| Práctica | Función a completar | Qué practicás |
|---|---|---|
| [01 · Extremos por mercado](energia/01_extremos_por_mercado.ipynb) | `extraer_extremos_por_mercado` | Trasladar el ejercicio de medianas a `Consumo` por `TipoConsumidor` |
| [02 · Serie mensual](energia/02_serie_mensual.ipynb) | `resumir_consumo_mensual` | Sumas mensuales, cobertura de datos y media móvil de 12 meses |
| [03 · Ranking de estados](energia/03_ranking_estados.ipynb) | `ranking_estados` | Top de UF por consumo y participación respecto del total general |
| [04 · Intensidad por mercado](energia/04_intensidad_por_mercado.ipynb) | `calcular_intensidad_por_mercado` | Agrupación temporal, faltantes emparejados y cociente de sumas |

## Datos y entorno

Los datasets ya están en `datos/`: `housing.csv` y `energia.xlsx`.
Conservá la carpeta completa, incluido `preparacion.py`; los ocho notebooks comparten
esa preparación y la caché de datos. Podés usarlos sin internet mientras esos archivos estén presentes.

Los archivos de datos se excluyen de Git. Si faltan al copiar o clonar el proyecto,
la primera ejecución los descarga desde las mismas fuentes públicas de los análisis:

- [California Housing Prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices).
- [Brazil's Energy Consumption](https://www.kaggle.com/datasets/lucasdasilvadantas/brazils-energy-consumption).

Se verificó que sus hashes coinciden con los registrados en los notebooks originales:
20.640 filas de viviendas y 285.499 registros de energía. La primera práctica de energía
usa las 271.811 filas donde ambas mediciones están presentes.

El entorno actual tiene las dependencias. En otro entorno, instalá
`python -m pip install -r requirements.txt` desde la raíz del proyecto y seleccioná ese kernel.

## Cómo interpretar las pruebas

Los casos pequeños tienen resultados esperados visibles para que puedas depurar sin recorrer
todo el dataset. Según el ejercicio, cubren empates, límites del filtro, grupos pequeños,
faltantes, fechas repetidas, meses ausentes, negativos o divisiones por cero.
También verifican que tu función conserve intacta la entrada.

Después se ejecuta tu función con los datos reales y se comprueban propiedades de la salida.
Las pruebas no sustituyen explicar tu razonamiento: revisá que el cálculo responda a la consigna.
Las funciones se entregan pendientes, con las pruebas verificadas mediante implementaciones
de referencia que no forman parte de estos materiales.
