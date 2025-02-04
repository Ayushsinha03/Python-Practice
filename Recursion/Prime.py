def prime(num,val=2):
    if val*val>num:
        return 'prime'
    if num%val==0:
        return 'not prime'
    return prime(num,val+1)
num = 11
print(prime(num))
