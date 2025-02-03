def int_binary(num,power=1,res=0):
    while num!=0:
        rem = num%2
        res = res+rem*power
        power = power*10
        num = num//2
    return res
num = 13
print(int_binary(num))
