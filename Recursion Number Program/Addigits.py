def addigits(num):
    if num==0:
        return 1
    return (num%10) + addigits(num//10)
num = 145
print(addigits(num))
