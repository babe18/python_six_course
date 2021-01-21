print("Please enter the upper base of the isosceles trapezoid:")
side1=float(input())
print("Please enter the bottom of the isosceles trapezoid:")
side2=float(input())
print("Please enter the height of the isosceles trapezoid:")
height=float(input())
area=(side1+side2)*height/2
hypotenuse=((((side2-side1)/2)**2)+(height**2))**0.5
perimeter=hypotenuse*2+side1+side2
print("The area of the isosceles trapezoid is {:.2f} \nThe perimeter of the isosceles trapezoid is {:.2f}".format(area,perimeter))