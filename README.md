# 📊 Análisis exploratorio de datos — Viviendas y Energía

> The Hatch · Challenge 1 · Python · pandas · seaborn

Dos análisis exploratorios (EDA) completos sobre datasets públicos, desde la limpieza hasta las conclusiones, más una serie de ejercicios de *livecoding* con sus resoluciones.

## 📓 Notebooks

| Notebook | Dataset | Qué se analiza |
|---|---|---|
| [`01_viviendas.ipynb`](notebooks/01_viviendas.ipynb) | [California Housing Prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices) | Distribuciones, valores faltantes e imputación, outliers, precio según la cercanía a la costa |
| [`02_energia.ipynb`](notebooks/02_energia.ipynb) | [Brazil's Energy Consumption](https://www.kaggle.com/datasets/lucasdasilvadantas/brazils-energy-consumption) | Serie mensual con media móvil, estacionalidad, ranking por estado y sector, mercado regulado frente a libre |

Cada notebook descarga su dataset y corre de punta a punta en memoria. Los resultados y gráficos ya están ejecutados y embebidos, así que se pueden leer directamente en GitHub.

## 🧪 Práctica de livecoding

| Carpeta | Contenido |
|---|---|
| [`practicas_livecoding/`](practicas_livecoding/) | 8 ejercicios cortos (4 por dataset): extremos por grupo, resúmenes, filtros por percentiles, sensibilidad a la imputación, rankings e intensidad |
| [`resoluciones_livecoding/`](resoluciones_livecoding/) | Resolución comentada de cada ejercicio |

## 🛠️ Stack

`Python` · `pandas` · `NumPy` · `matplotlib` · `seaborn` · `Jupyter`

## 🚀 Ejecutar

```bash
python -m pip install -r requirements.txt
jupyter notebook
```

Usá el mismo entorno de Python como kernel y ejecutá todas las celdas (*Restart & Run All*). Los notebooks necesitan internet para descargar los datos; en Kaggle activá internet y vinculá el dataset correspondiente.
