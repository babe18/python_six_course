weight = float(input("請輸入體重(kg):"))
height = float(input("請輸入身高(cm):"))
height_m = height/100
bmi = weight/(height_m**2)
print("你的BMI是{:.2f}".format(bmi))

