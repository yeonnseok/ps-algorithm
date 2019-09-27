a = [1, 4, 6, 3, 11, 7, 9, 10]


def selectionSort(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

print(selectionSort(a))
