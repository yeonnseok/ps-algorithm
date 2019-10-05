p, n = map(int, input().split())
a = list(map(int, input().split()))


left = 0
right = 200
while left <= right:
    mid = (left + right) // 2
    begin = end = 0
    end = n
    for i in range(n):
        end += mid//a[i]
    begin = end
    for i in range(n):
        if mid % a[i] == 0:
            begin -= 1
    begin += 1
    if p < begin:
        right = mid - 1
    elif p > end:
        left = mid + 1
    elif p == end:
        for i in range(n):
            if mid % a[i] == 0:
                if p == begin:
                    print(i + 1)
                    exit()
                begin += 1
