# 1) Write a program to check the string is palindrome or not with less number of itertion.
s = "malayalam"
for ind in range(0,len(s)):
    if s[ind]!= s[-ind-1]:
        print('not palindrome')
        break
else:
    print('palindrome')



# 2) Write a program to check the string is palindrome or not with while loop.
s = "madam"
ind = 0
while ind != len(s)//2:
    if s[ind]!= s[-ind-1]:
        print('not palindrome')
        break
    ind+=1
else:
    print('palindrome')


# 3) Write a program to check the given string is palindrome or not using while loop.
s = 'abcba'
res = ''
ind = len(s)-1
while ind!=-1:
    res = res+s[ind]
    ind-=1
if res==s:
    print('palindrome')
else:
    print('not palindrome')


# 4) Write a program to check the given string is palindrome or not using for loop.
s = 'madam'
res = ''
for ind in range(len(s)-1,-1,-1):
    res = res+s[ind]
if res==s:
    print('palindrome')
else:
    print('not palindrome')


# 5) Write a program to check given substring is palindrome or not  without using slicing.
s = 'madam'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        res = ''
        for ind in range(sv,ev):
            res = res+s[ind]
        rev = ''
        for ind1 in range(len(res)-1,-1,-1):
            rev = rev+res[ind1]
        if res==rev:
            print(rev)


            
    

