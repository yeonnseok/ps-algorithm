def solve(index, sum):
    if index == n:  # 무조건 3개를 더하되 하나는 그 중 선택할지말지는 2차적인 문제
        c[sum] = True
        return

    solve(index + 1, sum + a[index])
    solve(index + 1, sum)


n = int(input())
a = list(map(int, input().split()))
c = [False] * (n * 1000000 + 10)
solve(0, 0)
i = 1
while True:
    if c[i] is False:
        break
    i += 1
print(i)
