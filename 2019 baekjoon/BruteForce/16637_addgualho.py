# 괄호 안에는 연산자가 하나만 들어 있어야 하고, 중첩된 괄호는 사용할 수 없다.
# 괄호를 적절히 추가해서 만들 수 있는 결과의 최댓값을 구하는 문제
# 연산자의 갯수는 9개가 최대
# 먼저 계산한다 안한다 => 2^9 = 512개

n = int(input())
a = list(input())
for i in range(0, n, 2):
    a[i] = int(a[i])
m = (n-1)//2
ans = None
for s in range(1 << m):
    ok = True
    for i in range(m-1):
        if (s and (1 << i)) > 0 and (s and (1 << i + 1)) > 0:
            ok = False
    if not ok:
        continue
    b = a[:]
    for i in range(m):
        if (s and (1 << i)) > 0:
            k = 2*i + 1
            if b[k] == '+':
                b[k-1] += b[k+1]
                b[k+1] = 0
            elif b[k] == '-':
                b[k-1] -= b[k+1]
                b[k-1] = 0
            elif b[k] == '*':
                b[k-1] *= b[k+1]
                b[k] = '+'
                b[k+1] = 0
    temp = b[0]
    for i in range(m):
        k = 2 * i + 1
        if b[k] == '+':
            temp += b[k+1]
        elif b[k] == '-':
            temp -= b[k+1]
        elif b[k] == '*':
            temp *= b[k+1]
    if ans is None or ans < temp:
        ans = temp
print(ans)
