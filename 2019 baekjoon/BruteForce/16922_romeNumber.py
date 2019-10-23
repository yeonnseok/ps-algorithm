# 사용할 수 있는 문자의 갯수 4개
# 각 문자의 사용된 횟수가 같으면 같은 수다.
# 갯수만 정하면 된다.
# 4문자 합쳐 n개를 사용해야하므로 3문자의 갯수만 정해주면되므로 시간복잡도는 n^3으로 줄어든다.

n = int(input())
d = [False] * 1001

for i in range(n + 1):
    for j in range(n - i + 1):
        for k in range(n-i-j+1):
            l = n-i-j-k
            sum = i + 5*j + 10*k + 50 * l
            d[sum] = True
ans = 0
for i in range(len(d)):
    if d[i]:
        ans += 1
print(ans)