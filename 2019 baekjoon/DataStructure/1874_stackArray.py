def validate(li):
    for i in range(len(li) - 2):
        if (li[i] > li[i+2]) and (li[i+2] > li[i+1]):
            return "NO"
    return "YES"


n = int(input())
stackArray = []
for i in range(n):
    stackArray.append(int(input()))

idx = 0
ans = []

if validate(stackArray) == "NO":
    print("NO")
else:
    while stackArray:
        if idx < stackArray[0]:
            idx += 1
            ans.append('+')
        elif idx == stackArray[0]:
            ans.append('-')
            stackArray.pop(0)
        elif idx > stackArray[0]:
            ans.append('-')
            stackArray.pop(0)
    list(map(print, ans))


