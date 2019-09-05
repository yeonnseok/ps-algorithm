# from functools import reduce
#
#
# def findLasers(li):
#     lasers = []
#     for i in range(len(li)):
#         if li[i] == "(" and li[i+1] == ")":
#             lasers.append((i, i+1))
#     return lasers
#
#
# def add(a, b):
#     return a + b
#
#
# def findRods(li):
#     stack = []
#     rods = []
#     lasers = list(reduce(lambda x, y: add(x, y), findLasers(li)))
#     for i in range(len(li)):
#         if i in lasers:
#             continue
#         else:
#             if li[i] == "(":
#                 stack.append(i)
#             elif li[i] == ")":
#                 rods.append((stack.pop(), i))
#     return rods
#
#
# def main():
#     src = input()
#     lasers = findLasers(src)
#     rods = findRods(src)
#     count = 0
#     for i in range(len(rods)):
#         for j in range(len(lasers)):
#             if lasers[j][0] in list(range(rods[i][0], rods[i][1])):
#                 count += 1
#         count += 1
#     print(count)
#
#
# main()
#


def solve(src):
    stack = []
    count = 0
    for i in range(len(src)):
        if src[i] == "(":
            stack.append(i)
        elif src[i] == ")":
            if i - stack[-1] == 1:
                stack.pop()
                count += len(stack)
            else:
                stack.pop()
                count += 1
    return count


def main():
    src = list(input())
    print(solve(src))


main()
