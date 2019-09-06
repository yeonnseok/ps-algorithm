def solve(n, src):
    d = [0] * (n + 1)

    for i in range(1, n + 1):
        d[i] = 1
        for j in range(i):
            if src[j] < src[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    ans = []
    n = 4
    for i in reversed(range(1, len(src))):
        for j in reversed(range(1, max(d) + 1)):
            if d[i] == j and j == n:
                ans.insert(0, i)
                n -= 1

    array = []
    for i in ans:
        array.append(src[i])

    print(max(d))
    print(array)


def main():
    n = int(input())
    src = [0] + list(map(int, input().split()))
    print(solve(n, src))


main()
