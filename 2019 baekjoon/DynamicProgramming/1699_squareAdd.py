def solve(n):
    d = []
    count = 0
    for i in range(1, 1000):
        if i ** 2 > n:
            break
        d.append(i**2)

    for num in reversed(d):
        while num <= n:
            n -= num
            count += 1
    return count


def main():
    n = int(input())
    print(solve(n))


main()
