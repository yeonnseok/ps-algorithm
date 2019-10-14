n = int(input())
a = input().split()
check = [False] * 10
ans = []


def good(x, y, op):
    if op == ">":
        if x > y:
            return True
    elif op == "<":
        if x < y:
            return True
    return False


def recursive_budeng(index, num):
    if index == n + 1:
        ans.append(num)
        return

    for i in range(10):
        if check[i]:
            continue
        else:
            if index == 0 or good(num[index - 1], str(i), a[index - 1]):
                check[i] = True
                recursive_budeng(index + 1, num + str(i))
                check[i] = False


recursive_budeng(0, '')
ans.sort()
print(ans[-1])
print(ans[0])


