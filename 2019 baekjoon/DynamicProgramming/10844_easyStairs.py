def solve(n):
    # 길이가 i이고 마지막 자리수가 j인 계단수의 갯수
    d = []
    mod = 1000000000
    for _ in range(n + 1):
        d.append([0] * 10)

    # 1자리 계단수는 9개다.
    for i in range(1, 10):
        d[1][i] = 1

    for i in range(2, n + 1):
        for j in range(0, 10):
            # 경계조건1
            if j-1 >= 0:
                d[i][j] += d[i-1][j-1]
            # 경계조건2
            if j+1 < 10:
                d[i][j] += d[i-1][j+1]

    return sum(d[n]) % mod


def main():
    n = int(input())
    print(solve(n))


main()
