def disarum(num,dup,power,res=0):
    if num==0:
        return 'disarum number' if dup==res else 'not disarum number'
    rem = num%10
    res = res+(rem**power)
    return disarum(num//10,dup,power-1,res)
num = 135
power = len(str(num))
print(disarum(num,num,power))
