#身高體重2
weight = float(input("請輸入體重(kg):"))
height = float(input("請輸入身高(cm):"))
height_m = height/100
bmi = weight/(height_m**2)
print("你的BMI是{:.2f}".format(bmi))
if bmi<18.5:
    print("過輕")
elif bmi>=18.5 and bmi<24:
    print('標準')
else:
    print("過重")