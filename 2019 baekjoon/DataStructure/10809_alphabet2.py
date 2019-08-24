def alphabet_pos(word):
    ans = [-1] * 26
    for i in range(97, 123):
        if chr(i) in word:
            ans[i - 97] = word.index(chr(i))
    return ans


word = input()
print(alphabet_pos(word))

