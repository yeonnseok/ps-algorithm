MAX_SIZE = 16
decompressed = [[''] * MAX_SIZE for _ in range(MAX_SIZE)]
it = 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb'
idx = -1


def reverse(it):
    global idx
    idx += 1
    head = it[idx]
    if head == 'b' or head == 'w':
        return head
    upperLeft = reverse(it)
    upperRight = reverse(it)
    lowerLeft = reverse(it)
    lowerRight = reverse(it)
    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight


it = reverse(it)
idx = -1


def decompress(it, x, y, size):
    global idx
    idx += 1
    head = it[idx]
    if head == 'b' or head == 'w':
        for dx in range(size):
            for dy in range(size):
                decompressed[x+dx][y+dy] = head
    else:
        half = size//2
        decompress(it, x, y, half)
        decompress(it, x, y+half, half)
        decompress(it, x+half, y, half)
        decompress(it, x+half, y+half, half)


decompress(it, 0, 0, 16)
for row in decompressed:
    print(' '.join(row))
