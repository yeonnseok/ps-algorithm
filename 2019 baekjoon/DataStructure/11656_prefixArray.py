def prefixArray(word):
    arr = []
    for i in range(len(word)):
        arr.append(word[i:])
    arr.sort()
    return arr


word = input()
list(map(print, prefixArray(word)))
