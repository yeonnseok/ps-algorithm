n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))
ans = [0] * m


for k in range(len(b)):
    ans[k] = a.count(b[k])
print(ans)