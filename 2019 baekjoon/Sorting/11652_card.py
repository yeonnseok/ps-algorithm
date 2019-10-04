n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))
ans_cnt = 1
ans = cards[0]
cards.sort()
cnt = 1
for i in range(n-1):
    if cards[i] == cards[i+1]:
        cnt += 1
    else:
        cnt = 1
    if ans_cnt < cnt:
        ans_cnt = cnt
        ans = cards[i]
print(ans)


