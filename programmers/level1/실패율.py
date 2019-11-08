def solution(N, stages):
    fails = []
    stages.sort()
    for n in range(1, N + 1):
        length = len(stages)
        cnt = 0
        if length > 0:
            for i in range(length):
                if stages[i] == n:
                    cnt += 1
                else:
                    break
            fails.append((cnt / length, n))
            stages = stages[i:]

    fails = sorted(fails, key=lambda x: x[0], reverse=True)
    return list(list(zip(*fails))[1])