from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World perro"}

@app.get('/')
def genero(Año: str):
  datos = pd.read_csv("https://raw.githubusercontent.com/goodreads/goodreads-data/master/book_data.csv")
  datos = datos[datos["Year"] == Año]
  ventas = datos.groupby("Genre")["Ratings"].sum()
  ventas = ventas.sort_values(ascending=False)
  return ventas.head(5).index.to_list()

@app.get('/')
def juegos(Año: str):
  datos = pd.read_csv("https://raw.githubusercontent.com/SteamDB/steamdb/master/data/games.csv")
  datos = datos[datos["ReleaseDate"] >= Año]
  return datos["Name"].to_list()

@app.get('/')
def specs(Año: str):
  datos = pd.read_csv("https://raw.githubusercontent.com/SteamDB/steamdb/master/data/specs.csv")
  datos = datos[datos["Year"] == Año]
  usos = datos.groupby("Spec")["Count"].sum()
  usos = usos.sort_values(ascending=False)
  return usos.head(5).index.to_list()

@app.get('/')
def earlyacces(Año: str):
  datos = pd.read_csv("https://raw.githubusercontent.com/SteamDB/steamdb/master/data/games.csv")
  datos = datos[datos["ReleaseDate"] >= Año]
  early_access = datos[datos["EarlyAccess"] == True].count()["Name"]
  return early_access

@app.get('/')
def sentiment(Año: str):
  datos = pd.read_csv("https://raw.githubusercontent.com/SteamDB/steamdb/master/data/reviews.csv")
  datos = datos[datos["ReleaseDate"] >= Año]
  sentimientos = datos.groupby("Sentiment")["Count"].sum()
  sentimientos = sentimientos.sort_values(ascending=False)
  return sentimientos.head(5).index.to_list()