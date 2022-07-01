mobiles=open("mobiles.txt","r")
all_mobiles=[line.rstrip("\n").split(",") for line in mobiles]
print(all_mobiles)
# costly=max(all_mobiles,key=lambda m:int(m[2]))
# print(costly)
# least=min(all_mobiles,key=lambda m:int(m[2]))
# print(least)
fi_g=[mob for mob in all_mobiles if mob[3]=="5g"]
print(fi_g)