def int_binary(num,pos=1,res=0):
    if num==0:
        return res
    rem =(num%2)
    res = res+(rem*pos)
    return int_binary(num//2,pos*10,res)
num = 13
print(int_binary(num))
    
