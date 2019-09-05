# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)
#
#
# def factorial_count(num):
#     target = list(str(factorial(num)))
#     count = 0
#     for i in reversed(range(len(target))):
#         if target[i] == '0':
#             count += 1
#         else:
#             return count
#
#
# def main():
#     num = int(input())
#     print(factorial_count(num))
#
#
# main()


def main():
    num = int(input())
    i = 5
    ans = 0
    while i <= num:
        ans += int(num/i)
        i *= 5
    print(ans)


main()