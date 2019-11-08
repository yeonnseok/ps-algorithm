def solution(a, b):
    answer = ''
    day = 0
    day_name = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    idx = 0

    for i in range(1, a):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            day += 31
        elif i == 2:
            day += 28
        else:
            day += 30

    day += b
    idx += day % 7
    if a == 1 or a == 2:
        idx -= 1
    answer += day_name[idx]
    return answer