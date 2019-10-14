l, c = map(int, input().split())
a = input().split()
answer = []


def check(password):
    mo_cnt = 0
    ja_cnt = 0
    for ch in password:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            mo_cnt += 1
        else:
            ja_cnt += 1

    if mo_cnt >= 1 and ja_cnt >= 2:
        return True
    return False


def make_password(index, cur, answer):
    if len(cur) == l and index == c:
        if check(cur):
            cur.sort()
            answer.append(''.join(cur))

    if index >= c:
        return

    make_password(index + 1, cur + [a[index]], answer)
    make_password(index + 1, cur, answer)


make_password(0, [], answer)
answer.sort()
list(map(print, answer))