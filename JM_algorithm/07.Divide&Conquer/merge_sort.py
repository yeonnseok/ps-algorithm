def merge(a, b):
    new = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] >= b[j]:
            new.append(b[j])
            j += 1
        else:
            new.append(a[i])
            i += 1
    if a[i:]:
        new += a[i:]
    if b[j:]:
        new += b[j:]
    return new


def merge_sort(c):
    n = len(c)
    if n == 1:
        return c
    mid = n//2
    left = merge_sort(c[:mid])
    right = merge_sort(c[mid:])
    return merge(left, right)


li = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(li))

