n = 4
a = [list(map(int, list(input()))) for _ in range(n)]
k = int(input())
score = 0
for l in range(k):
    no, dir = map(int, input().split())
    no -= 1
    d = [0] * n
    d[no] = dir
    # 각 톱니는 동시에 회전해야하기 때문에 각 톱니들이 어떤 방향으로 회전해야하는지를 구하자.
    # 먼저 왼쪽 톱니들을 연쇄적으로 구하고
    for i in range(no-1, -1, -1):
        if a[i][2] != a[i+1][6]:  # 부호가 다르면
            d[i] = -d[i + 1]  # 반대 부호를 넣어줌,
        else:
            # 한 톱니가 회전하지 않으면 (부호가 같으면)
            # 그 톱니의 왼쪽에 있는 톱니도 회전하지 않는다.
            break
    # 오른쪽 톱니들도 마찬가지다.
    for i in range(no+1, n):
        if a[i-1][2] != a[i][6]:
            d[i] = -d[i - 1]
        else:
            break

    print(d)

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
        score += 2**i

print(score)
