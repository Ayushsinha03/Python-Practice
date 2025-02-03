def gcd(num1,num2):
    if num1<num2:
        gcd=num1
    else:
        gcd=num2
    while True:
        if num1%gcd==0 and num2%gcd==0:
            return gcd
        gcd-=1
num1 = 4
num2 = 6
print(gcd(num1,num2))
