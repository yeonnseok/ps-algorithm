from itertools import permutations


def check(perm, pred, strike, ball):
    s_cnt, b_cnt = 0, 0
    for i in range(3):
        if perm[i] == pred[i]:
            s_cnt += 1
        elif pred[i] in perm:
            b_cnt += 1
    if s_cnt == strike and b_cnt == ball:
        return True
    return False


def solution(baseball):
    answer = 0
    numbers = [i for i in range(1, 10)]
    perms = list(permutations(numbers, 3))

    for perm in perms:
        ans = 0
        for base in baseball:
            pred, strike, ball = list(map(int, list(str(base[0])))), base[1], base[2]
            if check(perm, pred, strike, ball):
                ans += 1
        if ans == len(baseball):
            answer += 1

    return answer