def solution(n):
    answer = ''
    w = '수박'
    l = len(w)
    if n % 2 == 0:
        answer += w*(n//l)
    else:
        answer += w*(n//l) + w[:n%l]
    return answer