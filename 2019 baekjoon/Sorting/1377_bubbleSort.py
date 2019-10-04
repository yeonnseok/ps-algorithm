n = 5
a = [[i] for i in range(n)]

for i in range(n):
    a[i].insert(0, int(input()))

a.sort()
ans = 0
for i in range(n):
    if a[i][1] - i > ans:
        ans = a[i][1] - i

print(ans + 1)
# change = False
#
# for i in range(n):
#     change = False
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             change = True
#             a[j], a[j+1] = a[j+1], a[j]
#     if not change:
#         print(i+1)
#         break

