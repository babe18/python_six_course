def Fibonacci(num):
    num1=1
    num2=1
    if(num==1 or num==2):
        print(1)
    elif(num>2):
        for i in range(num-2):
            newnum=num1+num2
            num1=num2
            num2=newnum
        print(newnum)
    else:
        print("error")

        
Fibonacci(int(input("請輸入你想看到費式數列的第幾項:")))