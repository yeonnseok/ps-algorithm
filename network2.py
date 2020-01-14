def cal_ans():
    temp = []
    ans = 0
    for i in range(len(src)):
        if src[i] == 0:
            if len(temp) == 5:
                temp = temp[1:]
            temp.append(i)
        else:
            ans += i * len(temp) - sum(temp)
            for j in temp:
                link[i + 1].append(j + 1)
                link[j + 1].append(i + 1)
    return ans


def cal_group():
    cnt, group = 0, 0
    zero_one = False
    start, end = -1, 0
    for i in range(len(src)):
        start = i + 1
        if src[i] == 1:
            group += 1
        else:
            break
    for i in range(len(src) - 1, -1, -1):
        end = i + 1
        if src[i] == 0:
            group += 1
        else:
            break
    for i in range(start, end):
        if src[i] == 0:
            cnt += 1
        elif src[i] == 1:
            if cnt >= 5:
                group += (cnt - 4)
            elif i >= 1 and src[i-1] == 0:
                zero_one = True
            cnt = 0
    if zero_one and len(src) != 1:
        return group + 1
    return group


num_of_case = int(input())
for case in range(1, num_of_case + 1):
    n = int(input())
    src = list(map(int, input().split()))
    link = [[] for _ in range(n + 1)]
    print("#%d" % case, end=" ")
    print(cal_ans(), end=" ")
    print(cal_group())

