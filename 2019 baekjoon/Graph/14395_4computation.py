from collections import deque

s, t = map(int, input().split())
# 경우의수가 많으므로 리스트보다 사전을 이용한다.

q = deque()
q.append((s, ''))
limit = 1000000000
d = set()
d.add(s)

while q:
    now, s = q.popleft()
    if now == t:
        if len(s) == 0:
            s = '0'
        print(s)
        exit()
    if 0 <= now * now <= limit and now * now not in d:
        q.append((now * now, s + '*'))
    if 0 <= now * now <= limit and now + now not in d:
        q.append((now + now, s + '+'))
    if 0 <= now * now <= limit and now - now not in d:
        q.append((now - now, s + '-'))
    if now != 0 and 0 <= now // now <= limit and now // now not in d:
        q.append((now // now, s + '/'))


