def is_possible(case, skill, dicts, check):
    for ch in case:
        if ch in skill:
            if check[dicts[ch] - 1] or dicts[ch] == 0:
                check[dicts[ch]] = True
            else:
                return False
    return True


def solution(skill, skill_trees):
    answer = 0
    dicts = {}
    for i in range(len(skill)):
        dicts[skill[i]] = i

    for case in skill_trees:
        check = [False] * len(skill)
        if is_possible(case, skill, dicts, check):
            answer += 1
    return answer