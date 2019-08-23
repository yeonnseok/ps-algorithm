stack = []

numOfOrder = int(input())

for i in range(numOfOrder):
    fullOrder = input().split()
    order = fullOrder[0]
    if order == 'push':
        stack.append(fullOrder[1])
    elif order == 'pop':
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)


