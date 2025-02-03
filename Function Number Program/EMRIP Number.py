def reverse(num,res=0):
    while num!=0:
        rem = num%10
        res = res*10+rem
        num = num//10
    return res
def prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return False
        return True
    return False
def EMIRP(num):
    var = reverse(num)
    if var!=num and prime(num) and prime(var):
        return 'EMIRP'
    return 'not EMIRP'
num = 17
print(EMIRP(num))
