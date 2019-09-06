# def solve(n):
#     count = 0
#     for i in range(1, n + 1):
#         if i < 10:
#             count += 1
#         elif i < 100:
#             count += 2
#         elif i < 1000:
#             count += 3
#         elif i < 10000:
#             count += 4
#         elif i < 100000:
#             count += 5
#         elif i < 1000000:
#             count += 6
#         elif i < 10000000:
#             count += 7
#         elif i < 100000000:
#             count += 8
#         else:
#             count += 9
#
#     return count


def solve(n):
    count = 0
    i, j = 1, 1
    while i <= n:
        if len(str(i)) > len(str(i - 1)):
            j += 1
        if i < 10 ** j:
            count += j
        i += 1
    return count


def main():
    n = int(input())
    print(solve(n))


main()
