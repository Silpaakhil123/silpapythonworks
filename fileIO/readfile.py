f=open("abc.txt")
# lst=[]
# for line in f:
#     lst.append(line)
# print(lst)

# out=list(f)
# print(out)

lines=[line.rstrip("\n") for line in f]
print(lines)
