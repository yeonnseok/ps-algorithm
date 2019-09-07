n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
first, second = [], []


def solve(index, first, second):
    # 정답일 경우
    if index == n:
        if len(first) != n//2:
            return -1
        if len(second) != n//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]

        return abs(t1-t2)

    # 불가능한 경우(백트래킹)
    if len(first) > n//2:
        return -1
    if len(second) > n//2:
        return -1

    # 다음 함수 호출
    ans = -1
    first.append(index)
    t1 = solve(index + 1, first, second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    first.pop()
    second.append(index)
    t2 = solve(index + 1, first, second)
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    second.pop()
    return ans


print(solve(0, first, second))