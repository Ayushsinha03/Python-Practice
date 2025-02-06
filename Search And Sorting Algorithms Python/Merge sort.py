l = [35,65,45,85,75,-45,96,25,-11,29]
def half(l):
    if len(l)>1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        half(left)
        half(right)
        merge_sort(l,left,right)
def merge_sort(l,left,right):
    lind,rind,mind=0,0,0
    while lind<len(left) and rind<len(right):
        if left[lind]<right[rind]:
            l[mind]=left[lind]
            lind+=1
        else:
            l[mind]=right[rind]
            rind+=1
        mind+=1
    while lind<len(left):
        l[mind]=left[lind]
        lind+=1
        mind+=1
    while rind<len(right):
        l[mind]=right[rind]
        rind+=1
        mind+=1
half(l)
print(l)
