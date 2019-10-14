k, *a = map(int, input().split())
print(a)


def lotto_num(index, cur):
    if len(cur) == 6:
        print(' '.join(map(str, cur)))
        return

    if index == 7:
        return

    lotto_num(index + 1, cur + [a[index]])
    lotto_num(index + 1, cur)


lotto_num(0, [])