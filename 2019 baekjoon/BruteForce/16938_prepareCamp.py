n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * 15
# 두 문제 이상을 골라야 한다.


def go(index, cnt, sum, easy, hard):
    if index == n:
        if cnt >= 2 and l <= sum and sum <= r and hard-easy >= x:
            return 1
        else:
            return 0
    cnt1 = go(index + 1, cnt + 1, sum+a[index], min(easy, a[index]), max(hard, a[index]))  # 고르는 것
    cnt2 = go(index + 1, cnt, sum, easy, hard)  # 고르지 않는 것
    return cnt1 + cnt2


print(go(0, 0, 0, -1, -1))