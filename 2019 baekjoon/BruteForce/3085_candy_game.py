# def swap_row(list, s, e):
#     temp = list[s]
#     list[s] = list[e]
#     list[e] = temp
#
#
# def find_length(n, src):
#     count = []
#     for i in range(n):
#         c_num, p_num, z_num, y_num = 1, 1, 1, 1
#         for j in range(n - 1):
#             if src[i][j] == "C" and src[i][j] == src[i][j + 1]:
#                 c_num += 1
#             if src[i][j] == "P" and src[i][j] == src[i][j + 1]:
#                 p_num += 1
#             if src[i][j] == "Z" and src[i][j] == src[i][j + 1]:
#                 z_num += 1
#             if src[i][j] == "Y" and src[i][j] == src[i][j + 1]:
#                 y_num += 1
#         count.append(max(c_num, p_num, z_num, y_num))
#
#     src = [list(i) for i in zip(*src)]
#     for i in range(n):
#         c_num, p_num, z_num, y_num = 1, 1, 1, 1
#         for j in range(n - 1):
#             if src[i][j] == "C" and src[i][j] == src[i][j + 1]:
#                 c_num += 1
#             if src[i][j] == "P" and src[i][j] == src[i][j + 1]:
#                 p_num += 1
#             if src[i][j] == "Z" and src[i][j] == src[i][j + 1]:
#                 z_num += 1
#             if src[i][j] == "Y" and src[i][j] == src[i][j + 1]:
#                 y_num += 1
#         count.append(max(c_num, p_num, z_num, y_num))
#
#     return max(count)
#
#
# def solve(n, src):
#     ans = []
#     for i in range(n):
#         for j in range(n - 1):
#             swap_row(src[i], j, j + 1)
#             ans.append(find_length(n, src))
#             swap_row(src[i], j, j + 1)
#
#             src = [list(i) for i in zip(*src)]
#             swap_row(src[i], j, j + 1)
#             ans.append(find_length(n, src))
#             swap_row(src[i], j, j + 1)
#     return max(ans)


def swap(first, second, src):
    temp = src[first[0]][first[1]]
    src[first[0]][first[1]] = src[second[0]][second[1]]
    src[second[0]][second[1]] = temp


def check(n, src):
    ans = 1
    for i in range(n):
        # 행에 대해 최대 길이 구함
        cnt = 1
        for j in range(1, n):
            if src[i][j] == src[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt: ans = cnt
        # 열에 대해 최대 길이 구함
        cnt = 1
        for j in range(1, n):
            if src[j][i] == src[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt: ans = cnt
    return ans


def main():
    n = int(input())
    src = []
    for _ in range(n):
        src.append(list(input()))
    ans = 0
    for i in range(n):
        for j in range(n):
            if j+1 < n:
                swap((i, j), (i, j + 1), src)
                temp = check(n, src)
                if ans < temp: ans = temp
                swap((i, j), (i, j + 1), src)
            if i+1 < n:
                swap((i, j), (i + 1, j), src)
                temp = check(n, src)
                if ans < temp: ans = temp
                swap((i, j), (i + 1, j), src)
    print(ans)


main()
