def fn_checkInput(side1,side2,side3):
    if(side1+side2<=side3 or side1+side3<=side2 or side2+side3<=side1):
        return False
    if(side1<=0 or side2<=0 or side3<=0):
        return False
    return True

def fn_getPerimeter(side1,side2,side3):
    if(fn_checkInput(side1,side2,side3)):
        return side1+side2+side3
    return "error"

def fn_getArea(side1,side2,side3):
    if(fn_checkInput(side1,side2,side3)):
        s=fn_getPerimeter(side1,side2,side3)/2
        return (s*(s-side1)*(s-side2)*(s-side3))**0.5
    return "error"

print("Please enter the length of the three sides of the triangle:")
side1=int(input())
side2=int(input())
side3=int(input())
area=fn_getArea(side1,side2,side3)
Perimeter=fn_getPerimeter(side1,side2,side3)
print("Area:", area)
print("Perimeter:", Perimeter)