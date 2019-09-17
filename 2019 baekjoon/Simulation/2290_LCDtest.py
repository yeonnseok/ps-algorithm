# 숫자는 모두 s+2의 가로와 2s+3의 세로로 이루어진다.
# 나머지는 공백으로 채워야 한다.
# 각 숫자사이에는 공백이 한칸 있어야 한다.
# -


s, n = input().split()
s = int(s)
n = list(n)
ans = []
while n:
    num = n.pop(0)
    a = [[' ']*(s + 2) for _ in range(2*s + 3)]

    for i in range(0, 2*s + 3):
            # 맨 윗줄
            if num == '0' or num == '2' or num == '3' or num == '5' or num == '6'or num == '7' or num == '8' or num == '9':
                for j in range(1, s + 1):
                    a[0][j] = '-'

            # 우측상단
            if num == '0' or num == '1' or num == '2' or num == '3' or num == '4' or num == '7' or num == '8' or num == '9':
                    if 1 <= i < s + 1:
                        a[i][-1] = '|'

            # 좌측 상단
            if num == '0' or num == '4' or num == '5' or num == '6' or num == '8' or num == '9':
                    if 1 <= i < s + 1:
                        a[i][0] = '|'

            # 중간줄
            if num == '2' or num == '3' or num == '4' or num == '5' or num == '6'or num == '8' or num == '9':
                for j in range(1, s + 1):
                    a[s+1][j] = '-'

            # 우측하단
            if num == '0' or num == '1' or num == '3' or num == '4' or num == '5' or num == '6'or num == '7' or num == '8' or num == '9':
                if s + 2 <= i < 2 * s + 2:
                    a[i][-1] = '|'

            # 좌측 하단
            if num == '0' or num == '2' or num == '6' or num == '8':
                if s + 2 <= i < 2 * s + 2:
                    a[i][0] = '|'

            # 맨 아랫줄
            if num == '0' or num == '2' or num == '3' or num == '5' or num == '6' or num == '8' or num == '9':
                for j in range(1, s + 1):
                    a[-1][j] = '-'

    for row in a:
        print(''.join(row))




