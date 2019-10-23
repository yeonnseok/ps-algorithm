from itertools import permutations

a, b = input().split()
perms = list(permutations(a))
ans = -1
for perm in perms:
    if perm[0] == '0':
        continue
    temp = int(''.join(perm))
    if temp > ans and temp < int(b):
        ans = temp

print(ans)