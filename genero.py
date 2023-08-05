import ast
import pandas as pd


rows = []
with open('steam_games.json') as f:
  for line in f.readlines():
    rows.append(ast.literal_eval(line))

df = pd.DataFrame(rows)

# json que va a consultar la funcion genero
generos_ano = ['genres', 'release_date']
df_genero = df[generos_ano].copy()
df_genero.fillna('', inplace=True)