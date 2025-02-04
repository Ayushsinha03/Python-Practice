def special(num,val=1,res=0):
    if val>num//2:
        return 'special number' if num==res else 'not special number'
    if num%val==0:
        res+=val
    return special(num,val+1,res)
num = 28
print(special(num))
