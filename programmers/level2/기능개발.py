def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    deploy = []

    for i in range(n):
        left = 100 - progresses[i]
        if left % speeds[i] == 0:
            deploy.append(left // speeds[i])
        else:
            deploy.append((left // speeds[i]) + 1)

    front = 0
    for idx in range(len(deploy)):
        if deploy[front] < deploy[idx]:
            answer.append(idx - front)
            front = idx
    answer.append(n - front)

    return answer