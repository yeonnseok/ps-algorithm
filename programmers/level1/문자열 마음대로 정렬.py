def solution(strings, n):
    answer = []
    m = len(strings)
    strings.sort()

    temp = []
    for i in range(m):
        temp.append((strings[i], strings[i][n]))
    temp = sorted(temp, key=lambda x: x[1])

    answer = list(list(zip(*temp))[0])
    return answer