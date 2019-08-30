def solve(n, src):
    d1 = [0] * (n + 1)
    d2 = [0] * (n + 1)
    for i in range(1, n + 1):
        d1[i] = 1
        for j in range(i + 1):
            if src[j] < src[i] and d1[j] + 1 > d1[i]:
                d1[i] = d1[j] + 1

    for i in reversed(range(1, n + 1)):
        d2[i] = 1
        for j in reversed(range(i, n + 1)):
            if src[j] < src[i] and d2[j] + 1 > d2[i]:
                d2[i] = d2[j] + 1
    ans = []
    for i in range(len(d1)):
       ans.append(d1[i] + d2[i] - 1)

    return max(ans)


def main():
    n = int(input())
    src = [0] + list(map(int, input().split()))
    print(solve(n, src))


main()
