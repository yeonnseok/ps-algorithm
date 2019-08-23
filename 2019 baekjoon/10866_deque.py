deque = []
numOfOrder = int(input())
for i in range(numOfOrder):
    fullOrder = input().split()
    order = fullOrder[0]
    if order == 'push_front':
        deque.insert(0, int(fullOrder[1]))
    elif order == 'push_back':
        deque.insert(-1, int(fullOrder[1]))
    elif order == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif order == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif order == 'size':
        print(len(deque))
    elif order == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(deque) == 0:
            print(-1)
        print(deque[0])
    elif order == 'back':
        if len(deque) == 0:
            print(-1)
        print(deque[-1])

#함수로 만들기 실패