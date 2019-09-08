from collections import deque

n = int(input())
dist = [[-1] * (n + 1) for _ in range(n + 1)]
q = deque()
q.append((1, 0))
dist[1][0] = 0  # 이모티콘 1개는 이미 화면에 띄워져 있음
while q:
    s, c = q.popleft()
    if dist[s][s] == -1:
        # 한개가 새로 복사 되었으면,,
        dist[s][s] = dist[s][c] + 1
        q.append((s, s))
    if s+c <= n and dist[s+c][c] == -1:
        # 한개가 붙여넣기 되었으면
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if 0 <= s-1 and dist[s-1][c] == -1:
        # 화면상의 이모티콘 한개를 삭제하면
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))

ans = -1
for i in range(1, n + 1):
    if dist[n][i] != -1:
        if ans == -1 or ans > dist[n][i]:
            ans = dist[n][i]

print(ans)


