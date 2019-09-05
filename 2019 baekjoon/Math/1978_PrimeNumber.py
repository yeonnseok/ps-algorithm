# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

#
# def solve(src):
#     count = 0
#     for i in range(len(src)):
#         if src[i] != 1 and src[i] != 0:
#             t_count = 0
#             for j in range(2, src[i]):
#                 if src[i] % j == 0:
#                     t_count += 1
#             if t_count == 0:
#                 count += 1
#     return count

#


def prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


def solve(n):
    count = 0
    for num in range(1, n+1):
        if prime(num):
            count += 1
    return count


def main():
    n = int(input())
    # src = list(map(int, input().split()))
    print(solve(n))

main()
