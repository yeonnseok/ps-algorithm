# def findNGF(arr, idx):
#     for i in range(idx, len(arr)):
#         if arr.count(arr[idx-1]) < arr.count(arr[i]):
#             return arr[i]
#     return -1
#
#
# def main():
#     numOfArr = int(input())
#     arr = list(map(int, input().split()))
#     ans = []
#     for idx in range(1, numOfArr+1):
#         ans.append(findNGF(arr, idx))
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
        while stack and (src.count(src[stack[-1]]) < src.count(src[i])):
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
