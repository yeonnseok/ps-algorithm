def solution(n):
    answer = 0
    che = [True] * (n+1)
    for i in range(2, n+1):
        for j in range(i+i, n+1,i):
            che[j] = False
    answer = che[2:].count(True)
    # answer = len([x for x in range(2, n+1) if che[x]])
    return answer