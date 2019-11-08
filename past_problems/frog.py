def solution(word):
    answer = ''
    wiki = {}  # wiki 라는 이름의 사전을 정의하고 청개구리 사전을 완성한다.
    j = 25
    for i in range(26):
        wiki[chr(65+i)] = chr(65+j)
        wiki[chr(97+i)] = chr(97+j)
        j -= 1

    # 주어진 단어의 각 문자들을 사전에 있는 지 검사하여 있으면 변환하여 answer에 더하고
    # 없다면(공백등의 알파벳 외의 문자) 그냥 추가한다.
    for ch in word:
        if ch in wiki:
            answer += wiki[ch]
        else:
            answer += ch
    return answer

print(solution('I love you'))
