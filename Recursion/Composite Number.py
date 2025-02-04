def composite(num,val=2):
    if val*val>num:
        return 'not composite'
    if num%val==0:
        return 'composite'
    return composite(num,val+1)
num = 51
print(composite(num))
