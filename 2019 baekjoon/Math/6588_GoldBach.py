# def is_primeNumber(num):
#     if num != 1:
#         t_count = 0
#         for idx in range(2, num):
#             if num % idx == 0:
#                 t_count += 1
#         if t_count == 0:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# def under_primeNumber(num):
#     arr = []
#     for i in range(1, num + 1):
#         if is_primeNumber(i):
#             arr.append(i)
#     return arr
#
#
# def devide_two_primeNumber(num):
#     pn = under_primeNumber(num)
#     for i in range(len(pn)):
#         for j in range(i + 1, len(pn)):
#             if pn[i] + pn[j] == num:
#                 return pn[i], pn[j]
#
#
# def main():
#     while 1:
#         num = int(input())
#         if num == 0:
#             break
#         else:
#             one, two = devide_two_primeNumber(num)
#             print(num, ' = ', one, ' + ', two)
#
#
# main()


def solve(num):
    if num != 5 and num % 2 == 1:
        return -1
    n = 100000
    prime = [0] * (n + 1)
    check = [0] * (n + 1)
    for i in range(2, n+1):
        if check[i] == 0:
            prime[i] = i
            for j in range(i*i, n + 1, i):
                check[j] = 1
    for i in range(n+1):
        for j in range(i, n+1):
            if prime[i] != 0 and prime[j] != 0 and prime[i] + prime[j] == num:
                return i, j


def main():
    while 1:
        num = int(input())
        if num == 0:
            break
        else:
            if solve(num) == -1:
                print("Goldbach's conjecture is wrong.")
            else:
                one, two = solve(num)
                print(num, ' = ', one, ' + ', two)


main()
