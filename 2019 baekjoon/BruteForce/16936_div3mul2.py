# 나3은 소인수분해시 3의 갯수가 줄어든다.
# 곱2는 소인수분해시 2의 갯수가 늘어난다.

n = int(input())
a = list(map(int, input().split()))

# 3의 갯수가 가장 많은 것이 가장 처음 와야한다.
# 어차피 연산의 종류가 나누기 3과 곱하기 2뿐이기 때문에 쉽게 구할 수 있다.

def three(num):
    cnt = 0
    while num > 1:
        if num % 3 == 0:
            cnt += 1
            num /= 3
        else:
            break
    return cnt


for i in range(n):
    a[i] = (a[i], three(a[i]))
a.sort()
a = sorted(a, key=lambda a: a[1], reverse=True)
ans = []
for i in range(n):
    ans.append(a[i][0])
print(ans)

