q = []
numOfOrder = int(input())
for i in range(numOfOrder):
    fullOrder = input().split()
    order = fullOrder[0]
    if order == 'push':
        q.append(int(fullOrder[1]))
    elif order == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(q) == 0:
            print(-1)
        print(q[0])
    elif order == 'back':
        if len(q) == 0:
            print(-1)
        print(q[-1])

#함수로 만들기 실패