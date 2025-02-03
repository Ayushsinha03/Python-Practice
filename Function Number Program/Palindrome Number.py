def palindrome(num,dup,res=0):
    while num!=0:
        rem = num%10
        res = res*10+rem
        num = num//10
    if dup==res:
        return 'palindrome'
    return 'not palindrome'
num = 12321
print(palindrome(num,num))
