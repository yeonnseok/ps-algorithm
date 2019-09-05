# def convert(word):
#     word = list(word)
#     for i in range(len(word)//2):
#         temp = word[i]
#         word[i] = word[-1-i]
#         word[-1-i] = temp
#     return ''.join(word)
#
#
# def pure_case(tg_sentence):
#     tg_sentence = tg_sentence.split()
#     for i in range(len(tg_sentence)):
#         tg_sentence[i] = convert(tg_sentence[i])
#     return ' '.join(tg_sentence)
#
#
# def diff_case(tg_sentence):
#     open = []
#     close = []
#     ans = []
#     for i in range(len(tg_sentence)):
#         if tg_sentence[i] == '<':
#             open.append(i)
#         elif tg_sentence[i] == '>':
#             close.append(i)
#     op = len(open)
#     ans.append(pure_case(tg_sentence[:open[0]]))
#     for i in range(op): #0, 1
#         ans.append(tg_sentence[open[i]:close[i] + 1])
#         if i + 1 > op - 1:
#             ans.append(pure_case(tg_sentence[close[i] + 1:]))
#         else:
#             ans.append(pure_case(tg_sentence[close[i] + 1:open[i+1]]))
#     return ''.join(ans)
#
#
# tg_sentence = input()
# if '<' not in tg_sentence and '>' not in tg_sentence:
#     print(pure_case(tg_sentence))
# else:
#     print(diff_case(tg_sentence))
#
#
# #뿌듯..
#
#


def solve(src):
    tag = False
    stack = []
    ans = []
    for i in range(len(src)):
        if src[i] == "<":
            tag = True
            while stack:
                ans.append(stack.pop())
            ans.append(src[i])
        elif src[i] == ">":
            tag = False
            ans.append(src[i])
        elif tag:
            ans.append(src[i])
        elif tag is False:  # tag is false
            stack.append(src[i])
        elif src[i] == " ":
            while stack:
                ans.append(stack.pop())
            ans.append(src[i])

    return ''.join(ans)


def main():
    src = input()
    print(solve(src))


main()
