def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    answer = [[''] * col for _ in range(row)]

    for r in range(row):
        for c in range(col):
            answer[r][c] = (arr1[r][c] + arr2[r][c])

    return answer