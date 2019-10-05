n = int(input())
a = list(map(int, input().split()))


a.sort()
b = []
t = 0
for i in range(len(a)):
    t += a[i]
    b.append(t)

print(sum(b))