def compare(num):
    num = list(map(int, list(str(num))))
    mul = 1
    for n in num:
        mul *= n
    return max(sum(num), mul)


def solution(pobi, crong):
    # 왼쪽은 홀수 오른쪽은 짝수
    # 포비가 이기면 1, 크롱이 이기면 2, 무승부는 0, 예외사항은 -1
    if pobi[1] - pobi[0] != 1 or crong[1] - crong[0] != 1:
        return -1

    pobi_score = max(compare(pobi[0]), compare(pobi[1]))
    crong_score = max(compare(crong[0]), compare(crong[1]))

    if pobi_score > crong_score:
        return 1
    elif pobi_score < crong_score:
        return 2
    elif pobi_score == crong_score:
        return 0
    else:
        return -1

pobi = [131, 132]
crong = [211, 212]
print(solution(pobi, crong))