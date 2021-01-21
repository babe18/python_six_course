import math
num = 2
while num < 1000:
    check = True
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            check = False
            break
        i = i + 1
    if True == check:
        print(num)
    num = num + 1

    