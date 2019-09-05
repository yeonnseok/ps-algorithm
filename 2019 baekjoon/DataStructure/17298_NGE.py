# def findNGE(arr, idx):
#     for i in range(idx, len(arr)):
#         if arr[idx-1] < arr[i]:
#             return arr[i]
#     return -1
#
#
# def main():
#     numOfArr = int(input())
#     arr = list(map(int, input().split()))
#     ans = []
#     for idx in range(1, numOfArr+1):
#         ans.append(findNGE(arr, idx))
#     print(ans)
#
#
# main()


def solve(n, src):
    stack = [0]
    ans = [0] * n
    for i in range(1, n):
        if len(stack) == 0:
            stack.append(i)
        while stack and (src[stack[-1]] < src[i]):
            ans[stack.pop()] = src[i]
        stack.append(i)

    while stack:
        ans[stack.pop()] = -1
    return ans


def main():
    n = int(input())
    src = list(map(int, input().split()))
    print(solve(n, src))


main()
