# 다 되는 경우의 수 - 안되는 경우의 수
# 같은 문자 or 숫자가 2번 연속해서 불가능하다.
# d => 10개
# d => 26개
# dd일 경우, 10 을 뺀다.
# 재귀함수를 이용해서 푼다.

s = input()


def go(s, index, last):
    if len(s) == index:
        return 1

    if s[index] == 'c':
        start = ord('a')
        end = ord('z')
    else:
        start = ord('0')
        end = ord('9')

    ans = 0
    for i in range(start, end+1):
        if i != last:
            ans += go(s, index + 1, i)
    return ans

print(go(s, 0, ''))


# ans = 0
# for i in range(len(s)):
#     cnt = 0
#     if s[i] == 'c':
#         cnt = 26
#     else:
#         cnt = 10
#
#     if i > 0 and s[i] == s[i-1]:
#         cnt -= 1
#     ans *= cnt

