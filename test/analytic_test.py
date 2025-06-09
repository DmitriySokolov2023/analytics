import requests
import pandas as pd
from sqlalchemy import create_engine

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

df.to_csv("output.csv", index=False)


df_read = pd.read_csv("output.csv")
engine = create_engine("postgresql://sokolov:SySHjAoLXO3SxLZa0WNiTRQqtwhQxz2W@dpg-d13h9v3e5dus73eoofug-a.frankfurt-postgres.render.com/analytics_ycdp")

df_read.to_sql("my_table", engine, if_exists="replace", index=False)