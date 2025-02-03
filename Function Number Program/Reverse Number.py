def reverse(num,res=0):
    while num!=0:
        rem = num%10
        res = res*10+rem
        num = num//10
    return res
num = 123
print(reverse(num))
