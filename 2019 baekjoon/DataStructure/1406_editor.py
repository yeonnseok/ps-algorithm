def editor(word, numOfOrder):
    cursor = len(word)
    for i in range(numOfOrder):
        fullOrder = input().split()
        order = fullOrder[0]
        if order == 'P':
            word.insert(cursor, fullOrder[1])
            cursor += 1
        elif order == 'L':
            cursor -= 1
            if cursor < 0:
                cursor = 0
        elif order == 'D':
            cursor += 1
        elif order == 'B':
            if cursor - 1 >= 0:
                del word[cursor - 1]
            cursor -= 1
    return ''.join(word)


word = list(input())
numOfOrder = int(input())

print(editor(word, numOfOrder))
