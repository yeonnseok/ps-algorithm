dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

a = [['U','R','L','P','M'],
     ['X','P','R','E','T'],
     ['G','I','A','E','T'],
     ['X','T','N','Z','Y'],
     ['X','O','Q','R','S']]


def hasWord(x, y, word):
    if x < 0 and y < 0 and x >= len(a) and y >= len(a[0]):
        return False
    if len(word) == 1:
        return True
    if a[x][y] != word[0]:
        return False

    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < len(a) and 0 <= ny < len(a[0]):
            if hasWord(nx, ny, word[1:]):
                return True
    return False

print(hasWord(1,1,'PRETTY'))