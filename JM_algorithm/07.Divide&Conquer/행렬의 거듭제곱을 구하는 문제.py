def identity(n):
    id = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                id[i][j] = 1
                break
    return id


def pow(a, m):
    if m == 0:
        return identity(len(a))
    if m % 2 > 0:
        return pow(a, m-1) * a
    half = pow(a, m//2)
    return half * half


a = [[4, 0], [1, 1]]
print(pow(a, 1))