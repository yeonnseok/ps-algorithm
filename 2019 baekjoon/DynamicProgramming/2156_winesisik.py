def solve(n, src):
    d = []
    for _ in range(n + 1):
        d.append([0] * 3)

    for i in range(1, n + 1):
        d[i][0] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])  # 저장..
        d[i][1] = d[i - 1][0] + src[i - 1]
        d[i][2] = d[i - 1][1] + src[i - 1]

    return max(d[-1])


def main():
    n = int(input())
    src = []
    for _ in range(n):
        src.append(int(input()))

    print(solve(n, src))


main()
