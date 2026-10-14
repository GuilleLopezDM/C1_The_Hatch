"""Carga compartida de los datasets para las prácticas de livecoding."""

from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

import pandas as pd


DATOS = Path(__file__).resolve().parent / "datos"


def _archivo(nombre, dataset, miembro):
    ruta = DATOS / nombre
    if not ruta.is_file():
        DATOS.mkdir(parents=True, exist_ok=True)
        url = f"https://www.kaggle.com/api/v1/datasets/download/{dataset}"
        print(f"Descargando {nombre} por primera vez...")
        with urlopen(url, timeout=90) as respuesta:
            contenido = respuesta.read()
        with ZipFile(BytesIO(contenido)) as comprimido:
            ruta.write_bytes(comprimido.read(miembro))
    return ruta


def cargar_viviendas():
    """Devuelve una base preparada nueva, conservando las filas y los índices."""
    ruta = _archivo(
        "housing.csv", "camnugent/california-housing-prices", "housing.csv"
    )
    df = pd.read_csv(ruta)
    df["ocean_proximity"] = df["ocean_proximity"].str.strip().str.upper()
    assert (df[["households", "total_rooms"]] > 0).all().all()

    df["bedrooms_imputados"] = df["total_bedrooms"].isna()
    df["total_bedrooms"] = df["total_bedrooms"].fillna(df["total_bedrooms"].median())
    df["rooms_per_household"] = df["total_rooms"] / df["households"]
    df["bedrooms_per_room"] = df["total_bedrooms"] / df["total_rooms"]
    df["population_per_household"] = df["population"] / df["households"]
    return df


def cargar_energia():
    """Devuelve la base mensual con faltantes, ceros y negativos conservados."""
    ruta = _archivo(
        "energia.xlsx",
        "lucasdasilvadantas/brazils-energy-consumption",
        "Dados brutos.xlsx",
    )
    base = pd.read_excel(ruta, engine="calamine")
    base = base.rename(columns={"Setor Econômico - N1": "Classe"})
    dimensiones = [
        columna for columna in base.columns
        if columna not in ["Data", "Consumo", "Consumidores"]
    ]
    for columna in dimensiones:
        base[columna] = base[columna].astype("string").str.strip()

    base["Data"] = pd.to_datetime(
        base["Data"].astype(str), format="%Y%m%d", errors="raise"
    )
    assert base["Data"].dt.day.eq(1).all()
    assert not base.duplicated(["Data"] + dimensiones).any()
    return base.sort_values("Data").set_index("Data")
