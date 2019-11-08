# 현재 암호문에 연속된 중복 문자열이 포함되어있는지를 검사한다.
def check_duple(word):
    n = len(word)
    for i in range(n-1):
        if word[i] == word[i+1]:
            return True
    return False


def solution(cryptogram):
    # 연속된 중복 문자열이 없을 때까지 반복문을 돌린다.
    while check_duple(cryptogram):
        n = len(cryptogram)
        d = [False] * n  # 현재 암호문의 길이만큼의 boolean 배열을 정의한다.
        temp = ''
        for i in range(n):
            cnt = 0
            for j in range(i+1, n):
                if cryptogram[i] == cryptogram[j]:
                    cnt += 1     # 연속으로 중복되는 값이 2개이상 있을 경우 검사를 시작하는 인덱스에 해당하는 d값도 True로 바꾸어준다.
                    d[j] = True  # 이중 반복문을 통해 연속으로 중복되는 문자의 인덱스에 해당하는 d값을 True로 바꿔준다.
                else:
                    break       # 연속이 끊기면 반복문을 빠져나온다.
            if cnt > 0:
                d[i] = True  # 연속되는 중복 문자열이 있었다면, 검사를 시작한 값도 True 로 바꿔준다.
        for i in range(n):
            if not d[i]:
                temp += cryptogram[i]  # 현재 문자열의 길이만큼을 순회하며 d값이 False인 값만 새로운 문자열인 temp에 추가한다.
        cryptogram = temp  # crpytogram에 temp를 대입해주고 다시 while 반복문을 수행한다.
    return cryptogram


cryptogram = "browoanoommnaon"
print(solution(cryptogram))