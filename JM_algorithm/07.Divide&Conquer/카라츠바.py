def normalize(num):
    num.append(0)
    for i in range(len(num)-1):
        if num[i] < 0:
            borrow = (abs(num[i]) + 9) // 10
            num[i+1] -= borrow
            num[i] += borrow * 10
        else:
            num[i+1] += num[i] // 10
            num[i] %= 10
    ans = []
    while num:
        ans.append(num.pop())
    return int(''.join(map(str, ans)))


def multiply(a, b):
    c = [0]*(len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    normalize(c)
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



a = [1,2,3,4]
b = [5,6,7,8]
print(karatsuba(a,b))