def swap_row(list, s, e):
    temp = list[s]
    list[s] = list[e]
    list[e] = temp


def find_length(n, src):
    count = []
    for i in range(n):
        c_num, p_num, z_num, y_num = 1, 1, 1, 1
        for j in range(n - 1):
            if src[i][j] == "C" and src[i][j] == src[i][j + 1]:
                c_num += 1
            if src[i][j] == "P" and src[i][j] == src[i][j + 1]:
                p_num += 1
            if src[i][j] == "Z" and src[i][j] == src[i][j + 1]:
                z_num += 1
            if src[i][j] == "Y" and src[i][j] == src[i][j + 1]:
                y_num += 1
        count.append(max(c_num, p_num, z_num, y_num))

    src = [list(i) for i in zip(*src)]
    for i in range(n):
        c_num, p_num, z_num, y_num = 1, 1, 1, 1
        for j in range(n - 1):
            if src[i][j] == "C" and src[i][j] == src[i][j + 1]:
                c_num += 1
            if src[i][j] == "P" and src[i][j] == src[i][j + 1]:
                p_num += 1
            if src[i][j] == "Z" and src[i][j] == src[i][j + 1]:
                z_num += 1
            if src[i][j] == "Y" and src[i][j] == src[i][j + 1]:
                y_num += 1
        count.append(max(c_num, p_num, z_num, y_num))

    return max(count)


def solve(n, src):
    ans = []
    for i in range(n):
        for j in range(n - 1):
            swap_row(src[i], j, j + 1)
            ans.append(find_length(n, src))
            swap_row(src[i], j, j + 1)

            src = [list(i) for i in zip(*src)]
            swap_row(src[i], j, j + 1)
            ans.append(find_length(n, src))
            swap_row(src[i], j, j + 1)
    return max(ans)


def main():
    n = int(input())
    src = []
    for _ in range(n):
        src.append(list(input()))
    print(solve(n, src))


main()
