import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df = pd.read_csv(filename,names=headers)

#print(df.describe())
#drive_wheels_counts = df["drive-wheels"].value_counts()
#print(drive_wheels_counts)
"""y = df["engine-size"]
x = df["price"]
plt.scatter(x,y)
plt.title("Scatterplot of Engine Size vs Price")
plt.xlabel("Engine Size")
plt.xlabel("Price")
plt.show()"""
df_test = df[["body-style","price"]]
df_grp = df_test.groupby(["body-style"],as_index=False).mean()
print(df_grp["price"])