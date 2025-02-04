def find_lcm(num1,num2,lcm=None):
    if lcm is None:
        lcm = max(num1,num2)
    if lcm%num1==0 and lcm%num2==0:
        return lcm
    return find_lcm(num1,num2,lcm+1)
print(find_lcm(4,6))
