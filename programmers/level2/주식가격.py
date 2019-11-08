def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        for j in range(1, n-i):
            if prices[i] > prices[i+j]:
                break
        if i == n-1:
            j = 0
        answer.append(j)
    return answer
