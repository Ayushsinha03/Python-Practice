def count(num,cout=0):
    while num!=0:
        num = num//10
        cout+=1
    return cout
num = 12345
print(count(num))
