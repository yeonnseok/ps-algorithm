

def quick_sort(a):
    n = len(a)
    if n == 1:
        return a
    if not a:
        return []
    pivot = a[0]
    left = []
    right = []

    for i in range(1, n):
        if a[i] >= pivot:
            right.append(a[i])
        else:
            left.append(a[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


a = [38, 27, 43, 9, 3, 82, 10]
print(quick_sort(a))