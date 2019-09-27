a = [1, 4, 6, 3, 11, 7, 9, 10]


def insertionSort(a):
    for i in range(len(a)):
        key = a[i]
        for j in range(i-1, -1, -1):
            if a[j] > key:
                a[j+1] = a[j]
                a[j] = key
    return a

print(insertionSort(a))
