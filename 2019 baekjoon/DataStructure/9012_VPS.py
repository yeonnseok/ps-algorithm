def validate(ps):
    open, close = 0, 0
    for i in range(len(ps)):
        if ps[i] == "(":
            open += 1
        elif ps[i] == ")":
            close += 1
    if open == close:
        return "YES"
    else:
        return "NO"


numOfCase = int(input())
ans = []
for i in range(numOfCase):
    #characters별로 분절하여 list에 담고싶으면 그냥 list(string)하면 된다.
    ps = list(input())
    ans.append(validate(ps))

list(map(print, ans))



