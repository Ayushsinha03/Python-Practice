def Prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return 'Not prime Number'
        return 'Prime Number'
    return 'Not Prime Number'
num = 2
print(Prime(num))
