def armstrong(num,dup,power,res=0):
    if num==0:
        return 'armstrong number' if dup==res else 'not armstrong number'
    rem = num%10
    res = res+rem**power
    return armstrong(num//10,dup,power,res)
num = 153
power = len(str(num))
print(armstrong(num,num,power))
