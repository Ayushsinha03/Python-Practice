def count(num,coun=0):
    if num==0:
        return coun
    return count(num//10,coun+1)
num = 12345
print(count(num))
