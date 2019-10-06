n, k = map(int, input().split())
jewerls = []
for _ in range(n):
    jewerls.append(list(map(int, input().split())))

jewerls = sorted(jewerls, key=lambda x: x[1], reverse=True)

bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()

ans = 0
idx = 0
while bags:
    if jewerls[idx][0] <= bags[0]:
        ans += jewerls[idx][1]
        del bags[0]
        idx += 1
    else:
        idx += 1

print(ans)