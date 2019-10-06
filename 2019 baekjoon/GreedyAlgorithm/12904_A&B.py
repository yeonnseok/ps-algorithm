s = list(input())
t = list(input())


def flip(a):
    new = []
    while a:
        new.append(a.pop())
    return new


while len(t) != len(s):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = flip(t)

if t == s:
    print(1)
else:
    print(0)

