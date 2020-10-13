import pandas as pd

filenew = open("new_songes.csv")
df = pd.DataFrame(filenew)
print(df)
