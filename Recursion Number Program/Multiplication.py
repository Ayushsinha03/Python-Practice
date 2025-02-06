def multiplication(num):
    if num==0:
        return 1
    return (num%10) * multiplication(num//10)
num = 145
print(multiplication(num))
