n = int(input())
a = list(map(int, list(input())))
b = list(map(int, list(input())))


def flip(a, x):
    for k in range(x-1, x + 2):
        if 0 <= k < len(a):
            a[k] = 1-a[k]


def go(a, b):
    ans = 0
    for i in range(len(a)-1):
        if a[i] != b[i]:
            flip(a, i + 1)
            ans += 1
    if a == b:
        return [True, ans]
    else:
        return [False, ans]


p1 = go(a, b)
flip(a, 0)
p2 = go(a, b)
if p2[0]:
    p2[1] += 1
if p1[0] and p2[0]:
    print(min(p1[1], p2[1]))
elif p1[0]:
    print(p1[1])
elif p2[0]:
    print(p2[1])
else:
    print("-1\n")
