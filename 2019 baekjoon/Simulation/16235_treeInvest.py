di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]  # 겨울에 추가되는 양분들
tree = [[{} for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v, age = map(int, input().split())  # 처음 심는 나무들 정보 (x좌표, y좌표, 나이)
    tree[u-1][v-1][age] = 1

g = [[5] * n for _ in range(5)]

for _ in range(k):
    # 0, 1, 2, 3

    for i in range(n):
        for j in range(n):
            # 봄
            if tree[i][j]:
                new_nutri = 0
                tmp = {}
                for age in sorted(tree[i][j].keys()):  # 어린나이 나무부터 양분을 먹는다.
                    if age * tree[i][j][age] <= g[i][j]:
                        tmp[age+1] = tree[i][j][age]
                        g[i][j] -= (age * tree[i][j][age])
                    else:
                        if g[i][j]:
                            tmp[age+1] = g[i][j]
                            g[i][j] -= (age * tmp[age+1])
                            if tree[i][j][age] - tmp[age+1]:
                                new_nutri += (age//2)
                        else:
                            new_nutri += (age//2)
                tree[i][j] = tmp
                g[i][j] += new_nutri

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                num = 0
                for age in tree[i][j].keys():
                    if not(age % 5):
                        num += tree[i][j][age]
                if num:
                    for k in range(8):
                        x = i + di[k]
                        y = j + dj[k]
                        if 0 <= x < n and 0 <= y < n:
                            if 1 not in tree[x][y].keys():
                                tree[x][y][1] = num
                            else:
                                tree[x][y][1] += num  # age 짜리 나무가 몇개 든 들어갈수 있다.

    for i in range(n):
        for j in range(n):
            g[i][j] += a[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += sum(tree[i][j].values())
print(cnt)