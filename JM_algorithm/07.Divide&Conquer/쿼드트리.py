def recursive(x, y, size):
    if size <= 1:
        return a[x][y]

    current_max = 0
    for i in range(size):
        for j in range(size):
            if a[x + i][y + j] > current_max:
                current_max = a[x + i][y + j]
    half = size // 2
    bm1 = recursive(x + half, y + half, half)
    bm2 = recursive(x + half, y, half)
    bm3 = recursive(x, y + half, half)
    bm4 = recursive(x, y, half)

    global ans, temp
    if size > 2:
        if current_max <= 1.2 * min(bm1, bm2, bm3, bm4):  # 등록
            if len(temp) < 4:
                temp.append(1)
            else:
                temp = [1] + temp[::-1]
                ans = temp + ans
                temp = []
        else:
            if len(temp) < 4:
                temp.append(0)
            else:
                ans = [0] + ans
                temp = []
    return current_max


no_of_case = int(input())
for case in range(1, no_of_case + 1):
    src = list(map(int, input().split()))
    n = src[0]
    a = []
    for i in range(n):
        a.append(src[1:][i * n: (i + 1) * n])
    ans, temp = [], []
    recursive(0, 0, n)

    print("#%d" % case, end=" ")
    ans = temp + ans
    for i in range(len(ans)):
        print("%d" % ans[i], end="")
    print()


