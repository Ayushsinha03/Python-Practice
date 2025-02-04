def perfect_square(num,val=1):
    if val*val>num:
        return 'not perfect_square number'
    if val*val==num:
        return 'perfect_square number'
    return perfect_square(num,val+1)
num = 16
print(perfect_square(num))
