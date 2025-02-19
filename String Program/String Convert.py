# 1) Write program to convert a string a alphbets into lowercase.
s = 'ABCdef'
res =''
for ch in s:
    if 'A'<=ch<='Z':
        res = res+chr(ord(ch)+32)
    else:
        res+=ch
print(res)

# 2) Write a program to convert in string a alphabets into uppercase.
s = 'acdDEF'
res = ''
for ch in s:
    if 'a'<=ch<='z':
        res = res+chr(ord(ch)-32)
    else:
        res+=ch
print(res)

# 3) Write a program to convert in string a (swapcase) in without using in bulit methods a given a substring.
s = 'AYUSH kumar SINHA'
res = ''
for ch in s:
    if 'A'<=ch<='Z':
        res = res+chr(ord(ch)+32)
    elif 'a'<=ch<='z':
        res = res+chr(ord(ch)-32)
    else:
        res+=ch
print(res)




