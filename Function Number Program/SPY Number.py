def spy(num,mul=1,res=0):
    while num!=0:
        rem = num%10
        res = res+rem
        mul = mul*rem
        num = num//10
    if res==mul:
        return 'SPY Number'
    return 'Not SPY Number'
num = 4
print(spy(num))
