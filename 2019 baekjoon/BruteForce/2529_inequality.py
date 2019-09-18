def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


def prev_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] >= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


def check(perm, a):
    for i in range(len(a)):
        if a[i] == '<' and perm[i] > perm[i+1]:
            return False
        if a[i] == '>' and perm[i] < perm[i+1]:
            return False
    return True


k = int(input())
a = input().split()
small = [i for i in range(k + 1)]
big = [9-i for i in range(k + 1)]

while True:
    if check(small, a):
        break
    if not next_permutation(small):
        break

while True:
    if check(big, a):
        break
    if not prev_permutation(big):
        break

print(''.join(map(str, big)))
print(''.join(map(str, small)))