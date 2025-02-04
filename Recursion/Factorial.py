def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)
num = 5
print(factorial(num))



def factorial(num,val=1,fact=1):
    if val==num+1:
        return fact
    return factorial(num,val+1,fact*val)
num = 5
print(factorial(num))
