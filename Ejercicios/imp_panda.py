import pandas as pd
import numpy as np



url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df = pd.read_csv(filename,names=headers)
df.replace("?",np.nan,inplace=True)

#print(df.describe(include="all"))
#df = pd.read_csv("vehiculos_parlamento.csv")
#df["TIPO"] = df["TIPO"].astype("string")
#df["length"]=df["length"]/df["length"].max()
#df["length"]=(df["length"]-df["length"].mean())/df["length"].std()

#print(df.info())

#missing_data = df.isnull()
#print(missing_data.head(5))
#print(df["length"])

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["horsepower"].replace(np.nan,avg_norm_loss,inplace=True)


df["horsepower"]=df["horsepower"].astype(int,copy=True)
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ["Low","Medium","High"]
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
#print(df['horsepower-binned'].value_counts)


#dummy_variable_1 = pd.get_dummies(df["fuel-type"])
#print(dummy_variable_1.head())
#print(pd.get_dummies(df["fuel-type"]).head(5))
#print(df["symboling"]+1)



