def lcm(num1,num2):
    if num1>num2:
        lcm=num1
    else:
        lcm=num2
    while True:
        if lcm%num1==0 and lcm%num2==0:
            return lcm
        lcm+=1
num1 = 4
num2 = 5
print(lcm(num1,num2))
