mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]
]
#q no: of mobiles
print(f"total no: of mobiles: {len(mobiles)}")

#q1 total number of out_of_stock mobiles
out_of_stk=[out_mob for out_mob in mobiles if out_mob[-1]==0]
print(f"total number of out_of_stock mobiles {len(out_of_stk)}")

#q2 total stock
total_stk=sum([mob[-1] for mob in mobiles])
print(f"total stock : {total_stk}")

# q3 print mobiles available in range 20k to 30k
ava_twe_thi=[avmob for avmob in mobiles if avmob[4]>=20000 and avmob[4]<=30000]
print(f" mobiles available in range 20k to 30k: {ava_twe_thi}")

# q4 print all 5g phone
fi_g_ph=[fi_g for fi_g in mobiles if fi_g[2]=="5g"]
print(f"5g phones: {fi_g_ph}")

# q5 print samsung mobiles
sam_mob=[sam for sam in mobiles if sam[5]=="samsung"]
print(f"samsung mobiles: {sam_mob}")

# q6 print costly mobile
max_price=max([cosmob[4] for cosmob in mobiles])
costly_mob=[cosmob for cosmob in mobiles if cosmob[4]==max_price]
print(costly_mob)

mobiles.sort(reverse=True,key=lambda m:m[4])
print(mobiles[0])

cost_pro=max(mobiles,key=lambda m:m[4])
print(cost_pro)

# q7 print low cost mobiles
mobiles.sort(reverse=True,key=lambda m:m[4])
print(mobiles[-1])

low_cost=min(mobiles,key=lambda m:m[4])
print(low_cost)

# q8 print all mobiles having stock >10
stk_ten=[mobls for mobls in mobiles if mobls[-1]>10]
print(f"mob having stock greater than 10: {stk_ten}")

# q9 count of mobiles having disply amoled
dis_amo=[amoled for amoled in mobiles if amoled[3]=="AMOLED"]
print(len(dis_amo))

# q10 sort mobiles based on price oredr by desc
mobiles.sort(reverse=True,key=lambda m:m[4])
print(mobiles)

# q11 sort mobiles based on avl stock oredr by asc
mobiles.sort(key=lambda m:m[4])
print(mobiles)

# q12 is there any mobile available at rs 10000 ?
mob_avl=[mob[4]==10000 for mob in mobiles]
print("available" if True in mob_avl else "na")

# q12 list all mobiles having same price