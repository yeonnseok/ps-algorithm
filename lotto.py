# 이곳에 소스코드를 작성하세요.
# Python3 만 지원됩니다.


def check_row(a, x, y):
    for number in a[x]:
        if a[x].count(number) > 1 and number == a[x][y]:
            return False
    return True


def check_col(a, x, y):
    col = [a[j][y] for j in range(9)]
    for number in col:
        if col.count(number) > 1 and number == a[x][y]:
            return False
    return True


def check_square(a, x, y):
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
    b = a
    for i in range(1, 10):
        b[x][y] = i
        if check_row(b, x, y) and check_col(b, x, y):
            return i


num_of_test = int(input())
for test in range(1, num_of_test + 1):
    answer = []
    k = int(input())
    a = [list(map(int, input().split())) for _ in range(9)]

    for x in range(9):
        for y in range(9):
            if not check_row(a, x, y) and not check_col(a, x, y):
                answer.append(x + 1)
                answer.append(y + 1)
                answer.append(find_answer(x, y))

    print("#%d" %test, end=" ")
    for x in answer:
        print(x, end=" ")
    print()



