n, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 한줄 한줄 검사,,
def go(a, l):
    n = len(a)
    c = [False] * n
    for i in range(1, n):
        if a[i-1] != a[i]:
            diff = abs(a[i-1] - a[i])
            if diff != 1:
                return False
            if a[i-1] < a[i]:
                for j in range(1, l + 1):
                    if i - j < 0:
                        return False
                    if a[i-1] != a[i-j]:
                        return False
                    if c[i-j]:
                        return False
                    c[i-j] = True  # 경사로 놓여진곳 체크
            else:
                for j in range(l):
                    if i + j > n:
                        return False
                    if a[i] != a[i+1]:
                        return False
                    if c[i+j]:
                        return False
                    c[i+j] = True
    return True


cnt = 0
for k in range(n):
    if go(a[k], l):
        cnt += 1
for k in range(n):
    d = [a[j][k] for j in range(n)]
    if go(d, l):
        cnt += 1


print(cnt)
