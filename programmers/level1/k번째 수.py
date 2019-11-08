def solution(array, commands):
    answer = []
    n = len(commands)

    for command in commands:
        i, j, k = command[0], command[1], command[2]
        temp = array[i - 1:j]
        temp.sort()
        answer.append(temp[k - 1])

    return answer