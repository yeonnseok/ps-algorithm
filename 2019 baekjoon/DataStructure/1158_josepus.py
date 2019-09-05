# def josepus(n, k):
#     q = []
#     ans = []
#     idx = 0
#     for i in range(1, n+1):
#         q.append(i)
#     while len(q) > 0:
#         idx += k - 1
#         ans.append(q.pop(idx))
#         if idx == len(q):
#             idx = 0
#         if idx + 2 >= len(q):
#             idx = -(idx + 2 - len(q))
#         if len(q) == k-1:
#             ans.append(q.pop(idx))
#         if len(q) == 1:
#             ans.append(q.pop())
#             break
#     return ans
#
#
# #애매하지만 일단 성공
# src = list(map(int, input().split()))
# print(josepus(src[0], src[1]))
#

import queue


def solve(src):
    n, k = src[0], src[1]
    q = queue.Queue()
    ans = []
    for i in range(1, n + 1):
        q.put(i)

    while q.qsize() != 0:
        for i in range(k-1):
            q.put(q.get())
        ans.append(q.get())
    return ans


def main():
    src = list(map(int, input().split()))
    print(solve(src))


main()
