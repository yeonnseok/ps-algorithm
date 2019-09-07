def check(password):
    # 최소 자음 두개 + 최소 모음 한개
    cnt_mo = 0
    cnt_ja = 0
    for i in range(len(password)):
        if (password[i] == 'a') or (password[i] == 'i') or (password[i] == 'o') or (password[i] == 'e') or (password[i] == 'u'):
            cnt_mo += 1
        else:
            cnt_ja += 1

        if (cnt_mo >= 1) and (cnt_ja >= 2):
            return True
    return False


def solve(L, al, password, i, ans):
    # 정답을 찾은 경우
    if len(password) == L:
        if check(password) and (''.join(password) not in ans):
            password.sort()
            ans.append(''.join(password))
            print(''.join(password))

    # 불가능한 경우
    if i >= len(al):
        return

    solve(L, al, password + [al[i]], i + 1, ans)
    solve(L, al, password, i + 1, ans)


def main():
    src = list(map(int, input().split()))
    L, C = src[0], src[1]
    al = input().split()
    password = []
    i = 0  # 사용할지 말지 결정해야하는 문자의 인덱스
    ans = []
    solve(L, al, password, i, ans)


main()