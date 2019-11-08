def solution(n, m):
    answer = []
    a, b = max(n, m), min(n, m)
    if a == b:
        return a

    while a % b != 0:
        a, b = b, a % b

    answer.append(b)
    answer.append(n * m // b)
    return answer