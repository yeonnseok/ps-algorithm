def multiply(a, b):
    c = [0]*(len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    return c

def karatsuba(a, b):
    an = len(a)
    bn = len(b)
    if an < bn:
        return karatsuba(b, a)
    if an == 0 or bn == 0:
        return
    if an <= 50:
        return multiply(a, b)
    half = an // 2
    a0 = a[:half]
    a1 = a[half:]
    b0 = b[:min(half, bn)]
    b1 = b[min(half, bn):bn]

    z2 = karatsuba(a1, b1)
    z0 = karatsuba(a0, b0)

    a0 = a0 + a1
    b0 = b0 + b1

    z1 = karatsuba(a0, b0)
    z1 -= z0
    z1 -= z2

    ret = z0 + z1*(10**half) + z2*(10**(2*half))
    return ret


def hugs(members, fans):
    n = len(members)
    m = len(fans)

    a = [0] * n
    b = [0] * m
    for i in range(n):
        if members[i] == "M":
            a[i] = 1
    for i in range(m):
        if fans[i] == 'M':
            b[i] = 1

    C = karatsuba(a, b)
    allHugs = C.count(0)
    return allHugs



members = 'FFFFF'
fans = 'FFFFFFFFFF'
print(hugs(members, fans))