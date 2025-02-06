def binary_int(num,pos=1,res=0):
    if num==0:
        return res
    rem = num%10
    res = res+(rem*pos)
    return binary_int(num//10,pos*2,res)
num = 1101
print(binary_int(num))
