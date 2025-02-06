l = [23,52,89,75,64,-4,-22,63,75,68]
def Selection_sort(l):
    for ind in range(len(l)):
        li = ind
        for ind2 in range(ind+1,len(l)):
            if l[ind2]<l[li]:
                li = ind2
        l[ind],l[li]=l[li],l[ind]
    return l
print(Selection_sort(l))
            
