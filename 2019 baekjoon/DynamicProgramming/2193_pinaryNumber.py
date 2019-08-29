def solve(n):
    d = []
    for i in range(n+1):
        d.append([0] * 2)
    # d[i][0] = d[i-1][0] + d[i-1][1]
    # d[i][1] = d[i-1][0]
    # 초기값 설정
    d[1][0] = 0
    d[1][1] = 1

    for i in range(2, n+1):
        for j in range(2):
            if j == 0:
                d[i][j] = d[i-1][0] + d[i-1][1]
            if j == 1:
                d[i][j] = d[i-1][0]

    return sum(d[n])


def main():
    n = int(input())
    print(solve(n))


main()
