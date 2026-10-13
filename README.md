# Entrega The Hatch C1

La entrega incluye estos archivos:

- `notebooks/01_viviendas.ipynb`
- `notebooks/02_energia.ipynb`
- `requirements.txt`

Instalá las dependencias desde la raíz del proyecto con
`python -m pip install -r requirements.txt`, usando el mismo entorno Python que el kernel.
Cada notebook descarga su dataset público desde internet y realiza el análisis completo en memoria. Los resultados están ejecutados y embebidos.
No necesitan carpetas de datos, scripts, documentos ni resultados externos.

Abrilos en Jupyter, Colab o Kaggle, reiniciá el kernel y ejecutá todas las celdas.
Necesitan un kernel Python con pip e internet. En Kaggle habilitá internet y vinculá
el dataset correspondiente al publicar, para cumplir los requisitos del challenge.

Fuentes:

- [Viviendas de California](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
- [Consumo de Brasil](https://www.kaggle.com/datasets/lucasdasilvadantas/brazils-energy-consumption)

Verificación del 13 de octubre de 2026: ambos notebooks ejecutados con kernels nuevos
y dependencias previamente instaladas; 25 celdas de código sin errores.
También se validaron la estructura de los notebooks, el lint y los enlaces y JavaScript de los HTML.
La evidencia de la ejecución anterior se conserva localmente en `.local/verificacion_internet/resultado.json`.

El repositorio también incluye las guías de estudio:

- `index.html`
- `explicacion_01_viviendas.html`
- `explicacion_02_energia.html`

Los materiales anteriores se conservaron en `.local/material_apoyo/`.
El ZIP anterior en `.local/entrega_notebooks.zip` no incluye estos cambios ni `requirements.txt`.
El repositorio excluye los materiales auxiliares y datos locales mediante `.gitignore`.
