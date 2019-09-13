n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]
k = int(input())
cnt = 0
for l in range(k):
    no, dir = map(int, input().split())
    no -= 1
    d = [0] * n
    d[no] = dir

    for i in range(no-1, -1, -1):
        if a[i][2] != a[i+1][6]:  # 부호가 다르면
            d[i] = -d[i + 1]  # 반대 부호를 넣어줌
        else:
            break

    for i in range(no+1, n):
        if a[i-1][2] != a[i][6]:
            d[i] = -d[i - 1]
        else:
            break

    for i in range(n):
        if d[i] == 0:
            continue
        if d[i] == 1:
            temp = a[i][7]
            for j in range(7, 0, -1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp
        elif d[i] == -1:
            temp = a[i][0]
            for j in range(7):
                a[i][j] = a[i][j+1]
            a[i][7] = temp


for i in range(n):
    if a[i][0] == 1:
        cnt += 1

print(cnt)
