# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)
#
#
# def combination_calculate(src):
#     n, m = src[0], src[1]
#     return int(factorial(n) / (factorial(m) * factorial(n-m)))
#
#
# def combination_zero_count(target):
#     count = 0
#     for i in reversed(range(len(target))):
#         if target[i] == '0':
#             count += 1
#         else:
#             return count
#
#
# def main():
#     src = list(map(int, input().split()))
#     combi_result = combination_calculate(src)
#     target = list(str(combi_result))
#     print(combination_zero_count(target))
#
#
# main()


def main():
    src = list(map(int, input().split()))
    n, m = src[0], src[1]
    two_n, two_nm, two_m = 2, 2, 2
    five_n, five_nm, five_m = 5, 5, 5
    two = 0
    five = 0

    while two_n <= n:
        two += int(n/two_n)
        two_n *= 2

    while two_nm <= n-m:
        two -= int((n-m)/two_nm)
        two_nm *= 2

    while two_m <= m:
        two -= int(m/two_m)
        two_m *= 2

    while five_n <= n:
        five += int(n / five_n)
        five_n *= 5

    while five_nm <= n - m:
        five -= int((n - m) / five_nm)
        five_nm *= 5

    while five_m <= m:
        five -= int(m / five_m)
        five_m *= 5

    print(min(two, five))


main()
