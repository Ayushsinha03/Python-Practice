l = [45,85,12,36,76,94,28,-4,70,-10,26]
def Bubble_sort(l):
    for ind in range(len(l)-1):
        for ind2 in range(len(l)-1-ind):
            if l[ind2]>l[ind2+1]:
                l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
    return l
print(Bubble_sort(l))
            
