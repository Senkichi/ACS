import pandas as pd

df = pd.read_csv("./final w lat lon.csv",encoding = "ISO-8859-1")

df = pd.to_numeric(df["Lon"])

df.to_json("./final w lat long.json",orient = "records")