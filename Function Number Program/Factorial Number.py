def factorial(num,fact=1):
    while num!=0:
        fact*=num
        num-=1
    return fact
num = 5
print(factorial(num))
