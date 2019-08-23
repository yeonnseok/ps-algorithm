def convert(word):
    word = list(word)
    for i in range(len(word)//2):
        temp = word[i]
        word[i] = word[-1-i]
        word[-1-i] = temp
    word = ''.join(word)
    return word


numOfSent = int(input())
ans = []
for i in range(numOfSent):
    bucket = input().split()
    for j in range(len(bucket)):
        bucket[j] = convert(bucket[j])
    sentence = ' '.join(bucket)
    ans.append(sentence)

#한줄로 리스트 내부 요소 하나씩 출력하기
list(map(print, ans))


