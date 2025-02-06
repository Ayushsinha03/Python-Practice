def prime(num,val=2):
    if val*val>num:
        return True
    if num%val==0:
        return False
    return prime(num,val+1)
def reverse(num,res=0):
    if num==0:
        return res
    rem = num%10
    res = res*10+rem
    return reverse(num//10,res)
def paliprime(num):
    if prime(num) and reverse(num)==num:
        return 'paliprime'
    return 'not paliprime'
num = 11
print(paliprime(num))
