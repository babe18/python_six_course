a=float(input("Enter a number:"))
b=float(input("Enter a number to divide by:"))
# print(f"The answer is {a/b}.")
try:
    print(f"The answer is {a/b}.")
except:
    print("This did not work .Did you try to divide by zero?")
else:
    print("You successfully divided two numbers.")
finally:
    print("Thank you")