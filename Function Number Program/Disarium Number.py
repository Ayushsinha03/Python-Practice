def disarium(num,dup,power,res=0):
    while num!=0:
        rem = num%10
        res = res+(rem**power)
        power-=1
        num = num//10
    if dup==res:
        return 'Disarium Number'
    return 'Not Disarium Number'
num = 135
power = len(str(num))
print(disarium(num,num,power))
