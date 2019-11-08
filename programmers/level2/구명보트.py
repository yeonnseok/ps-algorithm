def solution(people, limit):
    answer = 0

    people.sort()
    n = len(people)

    while people:
        if len(people) == 1:
            return answer + 1

        if people[0] + people[-1] <= limit:
            people.pop()
            people.pop(0)
            answer += 1
        else:
            people.pop()
            answer += 1

    return answer