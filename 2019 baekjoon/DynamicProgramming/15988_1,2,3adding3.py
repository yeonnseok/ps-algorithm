def solve(n):
    d = [0] * (n + 1)
    mod = 1000000009
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if d[n]:
        return d[n]

    d[n] = solve(n-1) + solve(n-2) + solve(n-3)
    return d[n] % mod


def main():
    numOfCase = int(input())
    for i in range(numOfCase):
        n = int(input())
        print(solve(n))


main()
