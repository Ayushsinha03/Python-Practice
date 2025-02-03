def Armstrong(num,dup,power,res=0):
    while num!=0:
        rem = num%10
        res = res+(rem**power)
        num = num//10
    if dup==res:
        return 'Armstrong Number'
    return 'Not Armstrong Number'
num = 153
power = len(str(num))
print(Armstrong(num,num,power))
