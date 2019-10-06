n = int(input())
a = list(map(int, input().split()))

d = [a[0]]

for i in range(1, n):
    left = 0
    right = len(d) - 1
    ans = d[right]
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if d[mid] >= a[i]:
            if ans >= d[mid]:
                ans = d[mid]
                idx = mid
                print("lower bound", ans)
            right = mid - 1
        else:
            left = mid + 1
    print(ans)

    if idx != -1:
        d[idx] = ans
    else:
        d.append(a[i])
print(len(d))

