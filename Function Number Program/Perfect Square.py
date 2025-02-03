def perfect_square(num):
    val = 0
    while val*val<=num:
        if val*val==num:
            return 'perfect square'
        val+=1
    return 'not perfect square'
num = 4
print(perfect_square(num))
    
            
