#聖誕樹2
height = int(input("Please input a integer:"))
stars = 1
if(height>=3 and height<=15):
    for i in range(height):
        print((' ' * (height - i)) + ('*' * stars))
        stars +=2
    print((' ' * height) + '|')
else:
    print('error')