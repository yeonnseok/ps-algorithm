n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))
ans = [0] * m


for k in range(len(b)):
    left = 0
    right = len(a) - 1
    print(left, right)
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == b[k]:
            ans[k] = 1
            break
        elif a[mid] > b[k]:
            right = mid - 1
        else:
            left = mid + 1

print(ans)