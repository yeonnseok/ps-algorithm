def solution(clothes):
    answer = 1
    n = len(clothes)

    dicts = {}
    for cloth in clothes:
        if cloth[1] not in dicts:
            dicts[cloth[1]] = 1
        else:
            dicts[cloth[1]] += 1

    for key in dicts:
        if len(dicts.keys()) > 1:
            answer *= (dicts[key] + 1)
        else:
            answer += dicts[key]
    return answer - 1