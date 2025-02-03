def binary_int(num,power=1,res=0):
    while num!=0:
        rem = num%10
        res = res+rem*power
        power = power*2
        num = num//10
    return res
num = 1101
print(binary_int(num))
