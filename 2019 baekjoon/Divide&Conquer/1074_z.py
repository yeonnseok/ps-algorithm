n, r, c = map(int, input().split())


def power2(k):
    return 1 << k


def go(n, x, y):
    if n == 1:
        return 2*x + y
    else:
        if x < power2(n-1):
            if y < power2(n-1):
                return go(n-1, x, y)
            else:
                return go(n-1, x, y-power2(n-1)) + power2(2*n-2)
        else:
            if y < power2(n-1):
                return go(n-1, x-power2(n-1), y) + power2(2*n-2)*2
            else:
                return go(n-1, x-power2(n-1), y-power2(n-1)) + power2(2*n-2)*3


print(go(n, r, c))
