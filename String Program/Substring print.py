# Write a program to print all the substring in a given string using silicing.
s = 'madam'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        print (s[sv:ev])


# Write a program to print all the substring without using silcing in a string.
s = 'madam'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        res = ''
        for ind in range(sv,ev):
            res = res+s[ind]
        print(res)
# Write a program to print the substring who length is even.
s = 'madam'
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        res = ''
        for ind in range(sv,ev):
            res = res+s[ind]
        if len(res)%2==0:
            print(res)

# Write a program to print largest substring in a string.
s = 'madam'
l = []
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        word = s[sv:ev]
        if word == word[::-1]:
            l.append(word)
print(max(l,key=len))


