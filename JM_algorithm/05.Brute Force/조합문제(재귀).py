

def pick(n, picked, topick):
    if topick == 0:
        print(' '.join(map(str, picked)))
    smallest = picked[-1] + 1 if picked else 1

    for nxt in range(smallest, n+1):
        picked.append(nxt)
        pick(n, picked, topick-1)
        picked.pop()  # 재귀는 다시 원상태로 돌려줘야한다.



pick(5, [], 3)