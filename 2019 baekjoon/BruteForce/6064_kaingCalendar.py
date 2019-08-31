def solve(numOfCase, src):
    m, n, x, y = src[0], src[1], src[2], src[3]
    yr = 1
    a, b = 1, 1
    while 1:
        if a == x and b == y:
            break

        if a < m:
            a += 1
        elif a >= m:
            a = 1
        if b < n:
            b += 1
        elif b >= n:
            b = 1

        if yr > 100000:
            return -1

        yr += 1
    return yr


def main():
    numOfCase = int(input())
    for _ in range(numOfCase):
        src = list(map(int, input().split()))
        print(solve(numOfCase, src))

main()
