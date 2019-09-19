def solve(a):
    n = len(a)
    # 종료 시점
    if n == 2:
        return 0
    ans = 0
    for i in range(1, n-1):
        energy = a[i-1] * a[i+1]
        b = a[:i] + a[i+1:]
        energy += solve(b)
        if ans < energy:
            ans = energy
    return ans


n = int(input())
a = list(map(int, input().split()))
print(solve(a))
