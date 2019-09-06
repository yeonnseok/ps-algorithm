def possible(c, breaks):
    if c == 0:
        if 0 in breaks:
            return 0
        else:
            return 1
    length = 0
    while c > 0:
        if c % 10 in breaks:
            return 0
        length += 1
        c //= 10
    return length


def main():
    n = int(input())
    m = int(input())
    breaks = list(map(int, input().split()))

    # 정답의 초기값
    ans = abs(n - 100)

    for i in range(1000001):
        length = possible(i, breaks)
        if length > 0:
            press = abs(i - n)

            if ans > length + press:
                ans = length + press
    print(ans)


main()


