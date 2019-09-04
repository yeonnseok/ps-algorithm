# def validate(ps):
#     open, close = 0, 0
#     for i in range(len(ps)):
#         if ps[i] == "(":
#             open += 1
#         elif ps[i] == ")":
#             close += 1
#     if open == close:
#         return "YES"
#     else:
#         return "NO"
#
#
# numOfCase = int(input())
# ans = []
# for i in range(numOfCase):
#     ps = list(input())
#     ans.append(validate(ps))
#
# list(map(print, ans))


def solve(src):
    stack = []
    for i in range(len(src)):
        if src[i] == "(":
            stack.append(src[i])
        else:
            try:
                stack.pop()
            except:
                return "NO"
    if stack:
        return "NO"
    else:
        return "YES"


def main():
    numOfCase = int(input())
    for _ in range(numOfCase):
        src = list(input())
        print(solve(src))


main()

