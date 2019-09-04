# def editor(word, numOfOrder):
#     cursor = len(word)
#     for i in range(numOfOrder):
#         fullOrder = input().split()
#         order = fullOrder[0]
#         if order == 'P':
#             word.insert(cursor, fullOrder[1])
#             cursor += 1
#         elif order == 'L':
#             cursor -= 1
#             if cursor < 0:
#                 cursor = 0
#         elif order == 'D':
#             cursor += 1
#         elif order == 'B':
#             if cursor - 1 >= 0:
#                 del word[cursor - 1]
#             cursor -= 1
#     return ''.join(word)
#
#
# word = list(input())
# numOfOrder = int(input())
#
# print(editor(word, numOfOrder))


def solve(n, exist):
    s_l = exist
    s_r = []
    for _ in range(n):
        fullOrder = input().split()
        if fullOrder[0] == "L":
            if s_l:
                s_r.insert(0, s_l.pop())
        elif fullOrder[0] == "D":
            if s_r:
                s_l.append(s_r.pop(0))
        elif fullOrder[0] == "P":
            s_l.append(fullOrder[1])
        elif fullOrder[0] == "B":
            if s_l:
                s_l.pop()

    return ''.join(s_l + s_r)


def main():
    exist = list(input())
    n = int(input())
    print(solve(n, exist))


main()