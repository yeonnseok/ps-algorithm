def to_binary(n, num):
    binary = []
    while num > 1:
        binary.append(num%2)
        num //= 2
    binary.append(num)
    while len(binary) < n:
        binary.append(0)
    binary = binary[::-1]
    return ''.join(map(str, binary))


def solution(n, arr1, arr2):
    answer = []
    length = len(arr1)
    for i in range(length):
        temp = ''
        bin1 = to_binary(n, arr1[i])
        bin2 = to_binary(n, arr2[i])
        for j in range(n):
            if bin1[j] == "1" or bin2[j] == "1":
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    return answer