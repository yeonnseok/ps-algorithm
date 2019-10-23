from itertools import permutations

a, b = input().split()
# perms = list(permutations(a))
# ans = -1
# for perm in perms:
#     if perm[0] == '0':
#         continue
#     temp = int(''.join(perm))
#     if temp > ans and temp < int(b):
#         ans = temp
#
# print(ans)

# 재귀를 이용한다면??
a = list(map(int, a))
n = len(a)
check = [False] * n
b = int(b)


def go(index, num):
    if index == n:
        return num
    ans = -1
    for i in range(n):
        if check[i]:  # 이미 사용한 수
            continue
        if index == 0 and a[i] == 0:  # 0으로 시작하면 안됨.
            continue
        check[i] = True
        temp = go(index + 1, num*10 + a[i])
        if temp < b:
            if ans == -1 or ans < temp:
                ans = max(ans, temp)
        check[i] = False
    return ans

print(go(0, 0))