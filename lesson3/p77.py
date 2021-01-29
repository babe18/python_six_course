# _input=int(input())
# print(factorial(_input))
def factorial(num):
    sum = 1
    for i in range(1, num + 1):
        sum *= i #sum=sum*i
    return sum
_input=int(input())
print(factorial(_input))