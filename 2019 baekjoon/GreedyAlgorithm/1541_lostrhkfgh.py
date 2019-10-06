a = list(input())

i = 0
stack = []
while i < len(a):
    if a[i] == '-':
        if not stack:
            a.insert(i+1, "(")
            stack.append(")")
        else:
            a.insert(i, stack.pop())

    if stack and i == len(a) - 1:
        a.append(stack.pop())
    i += 1

print(eval(''.join(a)))