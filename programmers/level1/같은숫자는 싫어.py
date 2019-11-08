def solution(arr):
    stack = []

    for n in arr:
        if not stack:
            stack.append(n)
        else:
            if stack[-1] != n:
                stack.append(n)
    return stack