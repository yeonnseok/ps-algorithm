def solution(heights):
    n = len(heights)
    answer = [0] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j + 1
                break
    return answer