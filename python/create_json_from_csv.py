import pandas as pd

df = pd.read_csv("./final w lat lon.csv",encoding = "ISO-8859-1")

df.to_json("./final w lat long.json")