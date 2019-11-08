def solution(number, k):
    answer = ''
    number = list(map(int, list(number)))

    while k > 0:
        if k >= len(number):
            return 0
        for i in range(len(number)-1):
            if number[i] < number[i+1]:
                number.pop(i)
                k -= 1
                break
    answer = ''.join(map(str, number))
    return answer