def solve(n):
    mod = 10007
    d = []
    for _ in range(n + 1):
        d.append([0] * 10)

    for i in range(10):
        d[1][i] = 1

    for i in range(1, n + 1):
        for j in range(10):
            for k in range(j+1):
                d[i][j] += d[i-1][k]  # 그 앞자리 수가 j+1 이하인것들의 합
    return sum(d[n])



def main():
    n = int(input())
    print(solve(n))


main()
