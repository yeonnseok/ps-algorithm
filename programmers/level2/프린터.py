def check(J, priorities):
    for p in priorities:
        if J[0] < p[0]:
            return False
    return True


def solution(priorities, location):
    answer = 0

    n = len(priorities)
    for i in range(n):
        priorities[i] = (priorities[i], i)

    cc = -1
    while location != cc and priorities:
        J = priorities.pop(0)
        if check(J, priorities):
            answer += 1
            cc = J[1]
        else:
            priorities.append(J)
    return answer