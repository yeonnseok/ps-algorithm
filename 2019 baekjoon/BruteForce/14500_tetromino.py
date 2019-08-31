def solve(n, m , src):
    ans = []
    for i in range(n):
        for j in range(m):
            if j + 3 < m:
                ans.append(src[i][j] + src[i][j+1] + src[i][j+2] + src[i][j+3])
            if i + 3 < n:
                ans.append(src[i][j] + src[i+1][j] + src[i+2][j] + src[i+3][j])
            if j + 2 < m:
                temp = src[i][j] + src[i][j+1] + src[i][j+2]
                if i - 1 > 0:
                    temp2 = temp + src[i - 1][j]
                    temp3 = temp + src[i - 1][j + 1]
                    temp4 = temp + src[i - 1][j + 2]
                    ans.append(temp2)
                    ans.append(temp3)
                    ans.append(temp4)
                if i + 1 < n:
                    temp2 = temp + src[i + 1][j]
                    temp3 = temp + src[i + 1][j + 1]
                    temp4 = temp + src[i + 1][j + 2]
                    ans.append(temp2)
                    ans.append(temp3)
                    ans.append(temp4)
            if j + 1 < m and i + 1 < n:
                ans.append(src[i][j] + src[i][j + 1] + src[i + 1][j] + src[i + 1][j + 1])
            # 10, 11, 12, 13, 14, 15
            if i + 2 < n:
                temp = src[i][j] + src[i + 1][j] + src[i + 2][j]
                if j + 1 < m:
                    temp2 = temp + src[i][j + 1]
                    temp3 = temp + src[i + 1][j + 1]
                    temp4 = temp + src[i + 2][j + 1]
                    ans.append(temp2)
                    ans.append(temp3)
                    ans.append(temp4)
                if j - 1 > 0:
                    temp2 = temp + src[i][j - 1]
                    temp3 = temp + src[i + 1][j - 1]
                    temp4 = temp + src[i + 2][j - 1]
                    ans.append(temp2)
                    ans.append(temp3)
                    ans.append(temp4)
            # 16, 17
            if i + 1 < n and j + 1 < m and j - 1 > 0:
                ans.append(src[i][j] + src[i][j+1] + src[i+1][j] + src[i+1][j-1])
                ans.append(src[i][j] + src[i][j-1] + src[i+1][j] + src[i+1][j+1])

            # 18, 19
            if i - 1 > 0 and j + 1 < m and i + 1 < n:
                ans.append(src[i][j] + src[i - 1][j] + src[i][j + 1] + src[i + 1][j + 1])
                ans.append(src[i][j] + src[i][j - 1] + src[i + 1][j - 1] + src[i - 1][j])

    return max(ans)


def main():
    inputs = list(map(int, input().split()))
    n, m = inputs[0], inputs[1]
    src = []
    for _ in range(n):
        aa = list(map(int, input().split()))
        src.append(aa)

    print(solve(n, m, src))


main()
