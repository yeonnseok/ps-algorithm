# O(NlogN) 분할정복
a = [-7, 4, -3, 6, 3, -8, 3, 4]


def fastMaxSum(a, lo, hi):
    if lo == hi:
        return a[lo]
    mid = (lo + hi) // 2
    left = 0
    right = 0
    sum = 0
    for i in range(mid, lo-1, -1):
        sum += a[i]
        left = max(left, sum)
    sum = 0
    for i in range(mid+1, hi+1):
        sum += a[i]
        right = max(right, sum)

    single = max(fastMaxSum(a, lo, mid), fastMaxSum(a, mid+1, hi))
    return max(left + right, single)


print(fastMaxSum(a, 0, len(a)-1))


# O(N) 동적계획법
n = len(a)
d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = max(d[i-1] + a[i-1], a[i-1])

print(max(d))