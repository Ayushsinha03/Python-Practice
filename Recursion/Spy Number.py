def spy(num,res=0,mul=1):
    if num==0:
        return 'spy number' if res==mul else 'not spy number'
    rem = num%10
    res = res+rem
    mul = mul*rem
    return spy(num//10,res,mul)
num = 123
print(spy(num))
