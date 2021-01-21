num = 2
while num <= 1000:
    check = True
    i = 2
    while i < num:
        if num % i == 0:
            check = False
        i = i + 1
    if True == check:
        print(num)
    num = num + 1