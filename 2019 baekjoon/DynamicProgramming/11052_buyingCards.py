# 돈을 최대한 많이 지불해서 카드 n개를 구매하려고 한다.
# 카드 i개가 포함된 카드팩의 가격은 Pi원이다.


def solve(src, n):
    d = [0] * (n + 1)
    if n <= 1:
        return src[0]

    if d[n]:
        return d[n]

    for i in range(1, n+1):
        for j in range(1, i+1):
            d[i] = max(d[i], d[i-j] + src[j])

    return d[n]


def main():
    n = int(input())
    src = [0] + list(map(int, input().split()))
    print(solve(src, n))


main()