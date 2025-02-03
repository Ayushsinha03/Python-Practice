def special(num,res=0):
    for val in range(1,num//2+1):
        if num%val==0:
            res+=val
    if num==res:
        return 'special number'
    return 'not a special number'
num = 6
print(special(num))
