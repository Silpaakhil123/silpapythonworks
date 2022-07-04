fmovies=open("movies.txt","r")
all_movies=[line.rstrip("\n").split(",") for line in fmovies]
print(all_movies)

# number of moviews released in 2022
mov_rel=[mov for mov in all_movies if mov[1]=="2022"]
print(len(mov_rel))

# number malayalam movies
mal_mov=[mov for mov in all_movies if mov[3]=="malayalam"]
print(mal_mov)

# theater released movies
th_mov=[mov for mov in all_movies if mov[4]=="theater"]
print(th_mov)

# list of movies whose rating > 5
rat_greater=[mov for mov in all_movies if mov[2]>="5"]
print(rat_greater)

# {2022:4,2021:6,2020:2}
released_yr={}
for line in all_movies:
    yr=line[1]
    if yr in released_yr:
        released_yr[yr]+=1
    else:
        released_yr[yr]=1
print(released_yr)

# 2021
out=max(released_yr.items(), key=lambda it:it[1])
print(out)
