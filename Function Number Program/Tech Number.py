def tech(num):
    if len(str(num))%2==0:
        num_str = str(num)
        mid = len(num_str)//2
        rh = int(num_str[mid:])
        lh = int(num_str[:mid])
        if (rh+lh)**2==num:
            return 'tech number'
        return 'not tech number'
    return 'not tech number'
num = 2025
print(tech(num))
