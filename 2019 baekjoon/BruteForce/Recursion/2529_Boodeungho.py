n = int(input())
a = input().split()
ans = []
check = [False] * 10


def good(x, y, op):
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True


def solve(index, num):
    if index == n+1:
        ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        if index == 0 or good(num[index-1], str(i), a[index-1]):
            check[i] = True
            solve(index+1, num+str(i))
            check[i] = False


solve(0, '')
ans.sort()
print(ans[-1])
print(ans[0])
