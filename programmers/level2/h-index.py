def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    n = len(citations)
    print(citations)

    for i in range(citations[0], 0, -1):
        for j in range(n):
            if citations[j] >= i and j + 1 >= i:
                return i
    return answer