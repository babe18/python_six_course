i = 1
while i <= 5:
    j = 1
    while j <= 5-i:
        print(" ", end="")
        j += 1
    y = 1
    while y <= 2*i -1:
        print("*", end="")
        y += 1
    print()
    i += 1

    