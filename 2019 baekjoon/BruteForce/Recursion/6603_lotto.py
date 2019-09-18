# 6개의 수를 고른다.


def go(a, index, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str, lotto)))
        return
    if index == len(a):
        return
    # 해당 인덱스번째 자리의 숫자를 선택하고 안하고 둘다 의미가 있으므로,,
    go(a, index + 1, lotto+[a[index]])
    go(a, index + 1, lotto)


while True:
    n, *a = list(map(int, input().split()))
    if n == 0:
        break
    go(a, 0, [])
    print()

