# 1) Write a program to remove a duplicate form a string.
s = 'raining'
res = ''
for ch in s:
    if ch not in res:
        res = res+ch
print(res)

# 2) Write a program to remove a duplicate form a string.
s = 'raining'
res = ''
ind = 0
while ind != len(s):
    if s[ind] not in res:
        res = res+s[ind]
    ind+=1
print(res)

# 3) Write a program to print occurences of every character from a string using for loop.
s = 'raining'
res = ''
for ch in s:
    if ch not in res:
        res = res+ch
for ch in res:
    print(f'{ch} - {s.count(ch)}')

# 4) Write a program to print occurences of every character from a string using while loop.
s = 'engineering'
res = ''
ind = 0
while ind!=len(s):
    if s[ind] not in res:
        res = res+s[ind]
    ind+=1
for ch in res:
    print(f'{ch}- {s.count(ch)}')

# 5) Write a program to print occurences of every character using replace methods.
s = 'raining'
while s!= '':
    print(f'{s[0]} - {s.count(s[0])}')
    s = s.replace(s[0],'')

#  6) Write a program to print the character which are having duplicate.
s = 'engineering'
res = ''
for ch in s:
    if ch not in res:
        res = res+ch
for ch in res:
    if s.count(ch)>1:
        print(ch)
    
