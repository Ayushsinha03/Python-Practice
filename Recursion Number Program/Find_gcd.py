def find_gcd(num1,num2,gcd=None):
    if gcd is None:
        gcd = min(num1,num2)
    if num1%gcd==0 and num2%gcd==0:
        return gcd
    return find_gcd(num1,num2,gcd-1)
print(find_gcd(4,6))
