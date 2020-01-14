from collections import deque


def check_network(i):
    max_cnt = 5
    global ans
    for j in range(index - 1, -1, -1):
        if src[j] == 0:
            ans += i - j
            link[i + 1].append(j + 1)
            link[j + 1].append(i + 1)
            max_cnt -= 1
        if max_cnt == 0:
            return


def bfs(start):
    q = deque()
    q.append(start)
    group[start] = True
    while q:
        x = q.popleft()
        for y in link[x]:
            if not group[y]:
                group[y] = True
                q.append(y)


num_of_case = int(input())
for case in range(1, num_of_case + 1):
    ans = 0
    n = int(input())
    src = list(map(int, input().split()))

    link = [[] for _ in range(n + 1)]
    for index in range(len(src)):
        if src[index] == 1:
            check_network(index)
    group = [False] * (n + 1)
    cnt = 0
    for start in range(1, n + 1):
        if not group[start]:
            bfs(start)
            cnt += 1

    print("#%d" % case, end=" ")
    print(ans, end=" ")
    print(cnt)

