import json
from functools import reduce
import random

with open("songs.json",encoding="utf-8") as f:
    data=json.load(f)
print(data)
# total no: of songs in album1
num_songs=[song for song in data if song["album"]=="album1"]
print(len(num_songs))

no_song=list(filter(lambda n:n["album"]=="album1",data))
print(len(no_song))

# highest rating song
# maxi=max(data,key=lambda n:n["rating"])
# print(maxi["rating"])
t_song=reduce(lambda s1,s2:s1 if s1["rating"]>s2["rating"] else s2,data)
print(t_song)
# high_rate=list(filter(lambda n:n["rating"]==maxi["rating"],data))
# print(high_rate)

# sad mode songs with random sample of 2
sad_s=list(filter(lambda s:s["mode"]=="sad",data))
print(sad_s)
rand_sad=random.sample(sad_s,2)
print(rand_sad)

# total number of albums
total_songs=set([s["album"] for s in data])
print(len(total_songs))

# which album containg most songs
alb={}
for s in data:
    if s["album"] in alb:
        alb[s["album"]]+=1
    else:
        alb[s["album"]]=1
print(alb)
print(max(alb.items(),key=lambda s:s[1]))

# most_s=reduce(lambda s1,s2:s1[])