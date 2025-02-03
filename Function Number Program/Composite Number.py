def composite(num):
    if num>3:
        for val in range(2,num//2+1):
            if num%val==0:
                return 'composite number'
        return 'not composite number'
    return 'not not composite number'
num = 51
print(composite(num))
