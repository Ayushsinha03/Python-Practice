def reverse(num,pos):
    if num==0:
        return 0
    return (num%10)*pos + reverse(num//10,pos//10)
def palindrome(num):
    if num==reverse(num,pos):
        return 'palindrome'
    return 'not palindrome'
num = 121
pos=10**(len(str(num))-1)
print(palindrome(num))
