list1=list(range(3,1001,3))
list2=list(range(7,1001,7))

# use loop 
res=0
for i in list1:
    res+=i
for i in list2:
    res+=i
print(res)

# use sum()
res=sum(list1)+sum(list2)
print(res)

