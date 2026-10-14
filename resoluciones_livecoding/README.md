# Resoluciones de las prácticas de livecoding

Ocho notebooks resueltos, con explicaciones, código comentado, pruebas y salidas guardadas.
Cada uno corresponde a una práctica de `practicas_livecoding`.

## Abrir y ejecutar

1. Abrí una resolución de la tabla.
2. Seleccioná el kernel de `.venv` del proyecto.
3. Usá **Reiniciar kernel y ejecutar todo**.

La sección **3. Resolución comentada** explica e implementa la función.
La sección **4. Pruebas y ejecución real** comprueba los casos de la práctica y ejecuta
la solución con el dataset completo. La variable `resultado` contiene la salida completa;
la tabla muestra hasta 20 filas. Ejecutá `display(resultado)` para inspeccionar más filas.

## Viviendas

| Resolución | Qué resuelve |
|---|---|
| [01 · Extremos por costa](viviendas/01_extremos_por_costa.ipynb) | Extrae las cinco filas más alejadas de la mediana de precio de cada `ocean_proximity` |
| [02 · Resumen por costa](viviendas/02_resumen_por_costa.ipynb) | Filtra por ingreso y calcula conteos y medianas por costa |
| [03 · Filtro por percentiles](viviendas/03_filtro_por_percentiles.ipynb) | Combina los cortes de tres ratios con la exclusión del precio máximo |
| [04 · Sensibilidad a la imputación](viviendas/04_sensibilidad_imputacion.ipynb) | Compara correlaciones con y sin filas imputadas |

## Energía

| Resolución | Qué resuelve |
|---|---|
| [01 · Extremos por mercado](energia/01_extremos_por_mercado.ipynb) | Extrae los consumos más alejados de la mediana por tipo de consumidor |
| [02 · Serie mensual](energia/02_serie_mensual.ipynb) | Calcula totales, cobertura y media móvil de doce meses |
| [03 · Ranking de estados](energia/03_ranking_estados.ipynb) | Obtiene las UF con mayor consumo y su participación en el total general |
| [04 · Intensidad por mercado](energia/04_intensidad_por_mercado.ipynb) | Calcula el cociente de sumas por mes y mercado con registros completos |

## Datos compartidos

Las resoluciones reutilizan `practicas_livecoding/preparacion.py` y los archivos ya descargados
en `practicas_livecoding/datos/`. Conservá ambas carpetas junto a la raíz del proyecto.
No hace falta ejecutar las prácticas ni los notebooks de análisis antes de abrir estas resoluciones.

Con los datasets presentes podés trabajar sin conexión. Si faltan, la preparación los descarga
desde Kaggle. En otro entorno, instalá las dependencias con
`python -m pip install -r requirements.txt` desde la raíz del proyecto.

Las pruebas conservan los casos originales: empates, límites de filtros, entradas vacías,
faltantes, índices temporales repetidos, negativos y denominadores inválidos, según el ejercicio.
También comprueban que las funciones no modifiquen el DataFrame recibido.
