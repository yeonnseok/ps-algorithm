def solution(money):
    answer = []
    unit = 50000
    sw = 1
    while unit >= 1:
        if unit != 5:
            answer.append(money//unit)
            money %= unit
        if sw == 1:
            unit //= 5
            sw = 0
        else:
            unit //= 2
            sw = 1
    return answer


def solution2(money):
    answer = []
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    for i in range(len(units)):
        answer.append(money // units[i])
        money %= units[i]
    return answer


print(solution2(50237))
