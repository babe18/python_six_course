def Fibonacci(num1,num2):
    if(num1<=0 or num2<=0):
        print("input error")
    else:
        print(num1)
        print(num2)
        for i in range(8):
            newnum=num1+num2
            print(newnum)
            num1=num2
            num2=newnum

num1=int(input("請輸入兩個整數當作費氏數列的開頭:"))
num2=int(input("請輸入兩個整數當作費氏數列的開頭:"))   
Fibonacci(num1,num2)
