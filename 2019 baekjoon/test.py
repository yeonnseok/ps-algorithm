T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = 1000
    def solve(x, y, total):
        global ans
        if x == n - 1 and y == n - 1:
            total += a[x][y]
            if ans > total:
                ans = total
            return
        if x < 0 or x >= n or y < 0 or y >= n:
            return

        solve(x + 1, y, total + a[x][y])
        solve(x, y + 1, total + a[x][y])
    solve(0, 0, 0)
    print('#%d' %test_case, ans)