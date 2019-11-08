def solution(number):
    cnt = 0
    for i in range(1, number+1):
        ch = str(i)
        cnt += (ch.count(str(3)) + ch.count(str(6)) + ch.count(str(9)))
    return cnt

print(solution(33))


