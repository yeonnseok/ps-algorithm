def next_permutation(src):
    n = len(src)
    i = n - 1
    while src[i-1] >= src[i]:
        i -= 1
    if i <= 0: return -1

    j = n - 1
    while src[i-1] >= src[j]:
        j -= 1
    src[i-1], src[j] = src[j], src[i-1]

    j = n - 1
    while i < j:
        src[i], src[j] = src[j], src[i]
        i += 1
        j -= 1
    return True


def calc(a, letters, d):
    m = len(letters)
    ans = 0
    alpha = dict()
    for i in range(m):
        alpha[letters[i]] = d[i]
    for s in a:
        now = 0
        for x in s:
            now = now * 10 + alpha[x]
        ans += now
    return ans


n = int(input())
a = ['']*n
letters = set()
for i in range(n):
    a[i] = input()
    letters |= set(a[i])
letters = list(letters)
m = len(letters)
d = [i for i in range(9, 9-m, -1)]
d.sort()
ans = 0
while True:
    now = calc(a, letters, d)
    if ans < now:
        ans = now
    if not next_permutation(d):
        break
print(ans)
