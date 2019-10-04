
def go(a, index, r, c, size):
    if size == 1:
        return r, c
    else:
        if a[index] == '1':
            return go(a, index, r, c+size//2, size//2)
        elif a[index] == '2':
            return go(a, index + 1, r, c, size//2)
        elif a[index] == '3':
            return go(a, index + 1, r+size//2, c, size//2)
        elif a[index] == '4':
            return go(a, index + 1, r+size//2, c+size//2, size//2)
    return 0, 0


def gogo(r, c, size, x, y):
    if size == 1:
        return ''

    if x < r+size//2 and y < c + size//2:
        return "2" + gogo(r, c, size//2, x, y)
    elif x < r+size//2 and y >= c + size//2:
        return "1" + gogo(r, c + size//2, size//2, x, y)
    elif x >= r + size//2 and y < c + size//2:
        return "3" + gogo(r+size//2, c, size//2, x, y)
    else:
        return "4" + gogo(r+size//2, c+size//2, size//2, x, y)


d, target = map(int, input().split())
x, y = map(int, input().split())

# 다시 풀기

