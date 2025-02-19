# 1) Write a program to reverse the string positive index.
s = 'hello'
res = ''
for ind in range(len(s)-1,-1,-1):
    res = res+s[ind]
print(res)

# 2) Write a program to reverse the string negative index.
s = 'hello'
res =''
for ind in range(-1,-len(s)-1,-1):
    res=res+s[ind]
print(res)

# 3) Write a program to reverse the string without using In-bulit method.
s = 'hello'
res = ''
for ch in s:
    res = ch+res
print(res)

# 4) Write a program to reverse the while loop negative index.
s = 'hello'
res = ''
ind = -1
while ind != -len(s)-1:
    res = res+s[ind]
    ind-=1
print(res)

# 5) Write a program to reverse the string using while loop positive index.
s = 'hello'
res = ''
ind = len(s)-1
while ind != -1:
    res = res+s[ind]
    ind-=1
print(res)
