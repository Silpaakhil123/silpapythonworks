import json
with open("countries.json",encoding="utf-8") as f:
    countries=json.load(f)
# print(countries)

# print total number of country details
print(len(countries))

# print languages of ukrane
lang=[country["languages"] for country in countries if country["name"]=="Ukraine"]
language=[lan["name"] for lan in lang[0]]
print(language)

# print currency of palestine
curr=[country["currencies"] for country in countries if country["name"].startswith("Palestine")]
currency=[curncy["name"] for curncy in curr[0]]
print(currency)

# print population of india
popu=[country["population"] for country in countries if country["name"]=="India"]
print(popu)

# print neighbouring countries of australia
neigh=[country["borders"] for country in countries if country["name"]=="Austria"]
print(neigh)

def get_coutry_data(country_name):
    return [country for country in countries if country["name"].lower().startswith(country_name)]

ind_data=get_coutry_data("india")
bord=ind_data[0].get("borders")
print(bord)
borders=[ country["name"] for country in countries if country["alpha3Code"] in bord]
print(borders)#border named countries

#maximum populated country
pop_coun=max(countries,key=lambda d:d.get("population"))
print(pop_coun["name"])

#minimum populated country
min_pop_coun=min(countries,key=lambda d:d.get("population"))
print(min_pop_coun["name"])
