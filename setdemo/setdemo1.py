lst=[10,12,1,14,1,12,15,15,16,16,14]
st=set(lst)
print(st)

st1={10,1,2,3,4,5}
st2={10,11,12,1,2}
uni_set=st1.union(st2)
print(uni_set)
int_set=st1.intersection(st2)
print(int_set)
dif_set=st1.difference(st2)
print(dif_set)

students=["ram","ravi","hari","tom","nikil","john","jain"]
passed_students=["ravi","hari","tom"]
st=set(students)
pst=set(passed_students)
fail_students=st.difference(pst)
# fail_students=st-pst
print(fail_students)

