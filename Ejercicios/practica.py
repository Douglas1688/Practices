import pandas as pd

songs = {"Artist":["Michael Jackson","AC/DC","Pink FLoyd","Whitney Houston","Meat Loaf","Eagles","Bee Gees","Fleetwood Mac"],
    "Album":["Thriller","Back in Black","The Dark Side of the Moon","The Bodyguard","Bat Out of Hell","Their Greatest Hits (1971-1975)","Saturday Night Fever","Rumours"],
         "Released":[1982,1980,1973,1992,1977,1976,1977,1977],
         "Length":["00:42:19","00:42:11","00:42:49","00:57:44","00:46:33","00:43:08","01:15:54","00:40:01"],
         "Genre":["Pop, rock, R&B","Hard rock","Progressive rock","R&B, soul, pop","Hard rock, progresive rock","rock, soft rock, folk rock","disco","soft rock"],
         "Music Recording Sales (Millions)":[46.0,26.1,24.2,27.4,20.6,32.2,20.6,27.9],
         "Claimed Sales (millions)":[65,50,45,44,43,42,40,40],
         "Released.1":["30-Nov-82","25-Jul-80","01-Mar-73","17-Nov-92","21-Oct-77","17-Feb-76","15-Nov-77","04-Feb-77"],
         "Soundtrack":["NaN","NaN","NaN","Y","NaN","NaN","Y","NaN"],
         "Rating":[10.0,9.5,9.0,8.5,8.0,7.5,7.0,6.5]}

#songs_frame = pd.DataFrame(songs)

df = pd.DataFrame(songs)
x= df[["Artist","Released"]]
print(x)
#x.to_csv("new_songes.csv")
x = df.iloc[1,0]
print(x)

"""
x = df.iloc[1,0]
print(x)

"""

"""i=0
print("\t Album")
for elem in songs["Album"]:
    print("",i,"",elem)
    i+=1"""
