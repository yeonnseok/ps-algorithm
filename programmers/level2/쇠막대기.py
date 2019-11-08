def solution(arrangement):
    count = 0
    stack = []
    n = len(arrangement)
    for i in range(n):
        if arrangement[i] == "(":
            stack.append(i)
        else:
            if i - stack[-1] == 1: # 레이저 발견
                stack.pop()
                count += len(stack)
            else:
                stack.pop()
                count += 1
    return count