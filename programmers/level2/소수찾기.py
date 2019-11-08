from itertools import permutations


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(map(int, list(numbers)))

    if sum(numbers) == 0:
        return 0

    n = len(numbers)
    temp = []
    for i in range(1, n + 1):
        perms = list(permutations(numbers, i))
        for num in perms:
            if int(''.join(map(str, num))) not in temp:
                temp.append(int(''.join(map(str, num))))
    for num in temp:
        if is_prime(num):
            answer += 1
    return answer 