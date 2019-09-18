def solve(index, sum):
    global cnt
    if index == n and sum == m:
        cnt += 1
        return
    if index == n and sum != m:
        return

    solve(index + 1, sum + a[index])
    solve(index + 1, sum)


n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
solve(0, 0)
# sum == 0 이면 처음부터 cnt 가 1올라가므로 1을 빼줘야함.
if m == 0:
    cnt -= 1
print(cnt)
