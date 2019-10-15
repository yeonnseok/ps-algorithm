n = int(input())
a = list(map(int, input().split()))
check = [False] * 100000


def solve(index, cur):
    if index == n:
        check[sum(cur)] = True
        return

    solve(index + 1, cur + [a[index]])
    solve(index + 1, cur)


solve(0, [])
for i in range(1, len(check)):
    if not check[i]:
        print(i)
        break
