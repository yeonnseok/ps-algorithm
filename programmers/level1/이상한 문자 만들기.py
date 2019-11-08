def solution(s):
    answer = ''
    idx = 0
    for ch in s:
        if idx % 2 == 0:
            answer += ch.upper()
        else:
            answer += ch.lower()
        idx += 1
        if ch == ' ':
            idx = 0

    return answer