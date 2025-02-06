def sample(num):
    if num==20:
        return
    if num%2==0:
        print(num,end=' ')
    return sample(num-1)
sample(1)
