check = [[False]*1501 for _ in range(1501)]
a, b, c = map(int, input().split())
s = (a + b + c)
if s % 3 != 0:
    print(0)
    exit()

# Target = a = b = c= (a+b+c)//3


def dfs(a, b):
    if check[a][b]:
        return
    check[a][b] = True
    p = [a, b, s-a-b]
    for i in range(3):
        for j in range(3):
            if p[i] < p[j]:
                b = [a, b, s-a-b]
                b[i] += a[i]
                b[j] -= a[i]
                dfs(b[0], [1])


if s % 3 != 0:
    print(0)
else:
    dfs(a, b)
    if check[s//3][s//3]:
        print(1)
    else:
        print(0)

