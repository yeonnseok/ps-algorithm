def ROT(sentence):
    for i in range(len(sentence)):
        pw = ord(sentence[i]) + 13
        # 대문자라면,
        if (ord(sentence[i]) >= 65) and (ord(sentence[i]) <= 90):
            if pw > 90:
                sentence[i] = chr(pw - 26)
            else:
                sentence[i] = chr(pw)
        # 소문자라면,
        elif (ord(sentence[i]) >= 97) and (ord(sentence[i]) <= 122):
            if pw > 122:
                sentence[i] = chr(pw - 26)
            else:
                sentence[i] = chr(pw)
    return ''.join(sentence)


sentence = list(input())
print(ROT(sentence))

