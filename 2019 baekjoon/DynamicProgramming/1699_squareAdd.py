# def solve(n):
#     d = []
#     count = 0
#     for i in range(1, 1000):
#         if i ** 2 > n:
#             break
#         d.append(i**2)
#
#     for num in reversed(d):
#         while num <= n:
#             n -= num
#             count += 1
#     return count


def solve(n):
    d = [0] * (n + 1)

    for i in range(1, n + 1):
        # 1^2 을 i개 사용한것이 최대 갯수
        d[i] = i
        j = 1
        while j*j < i:
            if d[i] > d[i - j*j] + 1:
                d[i] = d[i - j*j] + 1
            j += 1
    return d[n]


def main():
    n = int(input())
    print(solve(n))


main()
