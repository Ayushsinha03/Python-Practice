def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)
def square(num):
    if num==0:
        return 0
    return factorial(num%10) + square(num//10)
def strong(num):
    if num==square(num):
        return 'strong number'
    return 'not strong number'
num = 145
print(strong(num))
