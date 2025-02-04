def checkdigits(num):
    if num==0:
        return 0
    return (num%10)**2 + checkdigits(num//10)
def happy(num):
    if num>9:
        num = checkdigits(num)
        return happy(num)
    if num==1 or num==7:
        return 'happy number'
    return 'not happy number'
num = 13
print(happy(num))
