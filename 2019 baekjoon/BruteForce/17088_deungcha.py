n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()

ans = -1
for d1 in range(-1, 2):
    for d2 in range(-1, 2):
        change = 0  # 연산의 횟수 기록
        if d1 != 0:
            change += 1
        if d2 != 0:
            change += 1
        a0 = a[0] + d1  # 첫번째 항
        diff = (a[1] + d2) - a0  # 두번째 항
        ok = True
        an = a0 + diff
        for i in range(2, n):
            an += diff
            if a[i] == an:
                continue
            if a[i]-1 == an:
                change += 1
            elif a[i]+1 == an:
                change += 1
            else:
                ok = False
                break

        if ok:
            if ans == -1 or ans > change:
                ans = change
print(ans)

