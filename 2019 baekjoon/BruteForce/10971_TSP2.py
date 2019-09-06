def next_permutation(src):
    n = len(src)
    i = n - 1
    while src[i-1] >= src[i]:
        i -= 1

    if i <= 0: return -1

    j = n - 1
    while src[i-1] >= src[j]:
        j -= 1
    src[i-1], src[j] = src[j], src[i-1]

    j = n - 1
    while i < j:
        src[i], src[j] = src[j], src[i]
        i += 1
        j -= 1
    return True


def main():
    n = int(input())
    maps = []
    src = []
    for i in range(1, n+1):
        aa = [0] + list(map(int, input().split()))
        maps.append(aa)
        src.append(i)

    ans = 1000000
    while next_permutation(src) != -1:
        i = 0
        temp = 0
        for t in src:
            if maps[i][t] == 0:
                temp = 1000000
            else:
                temp += maps[i][t]
            i += 1
        if ans > temp:
            ans = temp
    print(ans)


main()
