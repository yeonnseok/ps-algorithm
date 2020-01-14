def check_row(x, y):
    check = [False] * 10
    for number in a[x]:
        if check[number] and number == a[x][y]:
            return False
        check[number] = True
    return True


def check_col(x, y):
    col = [a[j][y] for j in range(9)]
    check = [False] * 10
    for number in col:
        if check[number] and number == a[x][y]:
            return False
        check[number] = True
    return True


def check_square(x, y):
    check = [False] * 10
    seq = (x // 3) * 3 + (y // 3)
    for i in range(3):
        r = i + (seq // 3) * 3
        for j in range(3):
            c = j + (seq % 3) * 3
            if check[a[r][c]] and a[r][c] == a[x][y]:
                return False
            check[a[r][c]] = True
    return True


def find_answer(x, y):
    row = a[x]
    col = [a[j][y] for j in range(9)]

    first = []
    for i in range(1, 10):
        if i not in row and i != a[x][y]:
            first.append(i)

    second = []
    for i in range(1, 10):
        if i not in col and i != a[x][y]:
            second.append(i)

    if len(first) == 1:
        return first[0]
    if len(second) == 1:
        return second[0]


def check_correct(ans, x, y):
    temp = a[x][y]
    a[x][y] = ans
    if check_row(x, y) and check_col(x, y) and check_square(x, y):
        a[x][y] = temp
        return True
    a[x][y] = temp
    return False


def find_bug():
    for z in range(81):
        x, y = z // 9, z % 9
        if not check_row(x, y) and not check_col(x, y) and not check_square(x, y):
            ans = find_answer(x, y)
            if check_correct(ans, x, y):
                answer.append(x + 1)
                answer.append(y + 1)
                answer.append(ans)
        if len(answer) == k * 3:
            return


num_of_test = int(input())
for test in range(1, num_of_test + 1):
    k = int(input())
    a = [list(map(int, input().split())) for _ in range(9)]

    answer = []
    find_bug()
    print("#%d" % test, end=" ")
    for x in answer:
        print(x, end=" ")
    print()
