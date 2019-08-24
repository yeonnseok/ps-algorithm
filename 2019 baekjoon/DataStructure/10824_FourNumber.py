def FourPlus(src):
    return int(src[0] + src[1]) + int(src[2] + src[3])


src = input().split()
print(FourPlus(src))