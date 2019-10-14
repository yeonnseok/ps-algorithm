n, s = map(int, input().split())
a = list(map(int, input().split()))
answer = 0
# 재귀로 풀어보자


def recursive_sum(index, cur):
    global answer
    # base_case
    if index == n and cur == s:
        answer += 1
        return
    if index == n and cur != s:
        return

    recursive_sum(index + 1, cur + a[index])
    recursive_sum(index + 1, cur)


recursive_sum(0, 0)
# 맨처음 cur == 0일 때 아무것도 안 더하고 1이 추가 될수 있음.
if s == 0:
    answer -= 1
print(answer)