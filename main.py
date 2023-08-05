from typing import Union
import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World perrito"}

@app.get('/generos')
def genero(Año: str):
  datos = pd.read_json("steam_games.json")
  datos = datos[datos["Year"] == Año]
  ventas = datos.groupby("Genres")["release_date	"].sum()
  ventas = ventas.sort_values(ascending=False)
  return ventas.head(5).index.to_list()
