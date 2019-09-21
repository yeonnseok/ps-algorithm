# 14890 경사로

n, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def check(a, l):
    c = [False] * len(a)
    for i in range(1, len(a)):

        if a[i - 1] != a[i]:

            diff = abs(a[i - 1] - a[i])
            if diff != 1:
                return False

            if a[i - 1] < a[i]:
                for j in range(1, l + 1):
                    if i - j < 0:
                        return False
                    if a[i - 1] != a[i - j]:
                        return False
                    if c[i - j]:
                        return False
                    c[i - j] = True
            else:
                for j in range(l):
                    if i + j > n:
                        return False
                    if a[i] != a[i + j]:
                        return False
                    if c[i + j]:
                        return False
                    c[i + j] = True

        return True


ans = 0
for row in a:
    if check(row, l):
        ans += 1

# for k in range(n):
#     col = [a[j][k] for j in range(n)]
#     if check(col, l):
#         ans += 1
print(ans)
