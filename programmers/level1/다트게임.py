def score_cal(info):
    dicts = {'S': 1, "D": 2, "T": 3}
    for i in range(len(info)):
        if info[i][-1] == "#":
            info[i] = -int(info[i][0]) ** dicts[info[i][1]]
        elif info[i][-1] == "*":
            if i >= 1:
                info[i - 1] *= 2
            info[i] = 2 * (int(info[i][0])) ** dicts[info[i][1]]
        else:
            info[i] = int(info[i][0]) ** dicts[info[i][1]]
    return sum(info)


def solution(dartResult):
    answer = 0
    n = len(dartResult)

    info = []
    temp = []
    for ch in dartResult:
        if ch not in "SDT*#":
            if not temp:
                temp = [ch]
            else:
                try:
                    int(temp[-1])
                    temp[-1] += ch
                except:
                    info.append(temp)
                    temp = [ch]
        else:
            temp.append(ch)
    if temp:
        info.append(temp)

    answer = score_cal(info)
    return answer