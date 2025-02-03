def square(num,res=0):
    while num!=0:
        rem = num%10
        res = res+rem**2
        num = num//10
    return res
def happy(num):
    while num>9:
        num = square(num)
    if num==1 or num==7:
        return 'happy number'
    return 'not happy number'
num = 13
print(happy(num))
        
