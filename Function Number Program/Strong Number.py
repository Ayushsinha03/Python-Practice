def factorial(num,fact=1):
    while num!=0:
        fact*=num
        num-=1
    return fact
def adding(num,res=0):
    while num!=0:
        rem = num%10
        res = res+factorial(rem)
        num = num//10
    return res
def strong(num):
    if adding(num)==num:
        return 'strong number'
    return 'not strong number'
num = 145
print(strong(num))
