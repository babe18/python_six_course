#while loop
i=1
while i<=100:
    if i%5==0:
        i+=1
        continue
    print(i)
    i+=1

#for loop
for i in range(1,101):
    if i%5==0:
        continue
    print(i)

