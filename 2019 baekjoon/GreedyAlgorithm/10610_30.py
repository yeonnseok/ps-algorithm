n = int(input())

s = str(n)

is_three = []
for i in range(len(s)):
    num = int(s[i])
    is_three.append(num)


if sum(is_three) % 3 == 0:
    ans = sorted(is_three, reverse=True)
    if ans[-1] == 0:
        print(int(''.join(map(str, ans))))
    else:
        print(-1)
else:
    print(-1)

