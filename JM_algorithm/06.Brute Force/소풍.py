n, m = 4, 6
a = [0, 1, 1, 2, 2, 3, 3, 0, 0, 2, 1, 3]
s = [i for i in range(n)]
areFriends = [[False] * n for _ in range(n)]
for i in range(0, 2*m-1, 2):
    areFriends[a[i]][a[i+1]] = True
    areFriends[a[i+1]][a[i]] = True

for row in areFriends:
    print(' '.join(map(str,row)))
check = [False] * n
# 무조건 2명씩 짝지어주면됨


def soulmate(check):
    firstFree = -1
    for i in range(n):
        if not check[i]:
            firstFree = i
            break
    if firstFree == -1:
        return 1
    ret = 0
    for pairwith in range(firstFree+1, n):
        if not check[pairwith] and areFriends[firstFree][pairwith]:
            check[pairwith] = check[firstFree] = True
            ret += soulmate(check)
            check[pairwith] = check[firstFree] = False
    return ret

print(soulmate(check))

