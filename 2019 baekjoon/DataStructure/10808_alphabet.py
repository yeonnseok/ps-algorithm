def alphabet(word):
    ans = [0] * 26
    for i in range(97, 123):
        ans[i - 97] = word.count(chr(i))
    return ans


word = input()
print(alphabet(word))