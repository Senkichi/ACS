import pandas as pd

df = pd.read_csv("./final_w_lat_lon.csv")

df.to_json("./final_w_lat_lon.json",orient = "records")