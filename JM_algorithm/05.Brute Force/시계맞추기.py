clocks = [12, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
con = [[0, 1, 2], [3, 7, 9, 11], [4, 10, 14, 15], [0, 4, 5, 6, 7], [6, 7, 8, 10, 12], [0, 2, 14, 15], [3, 14, 15], [4, 5, 7, 14, 15], [1, 2, 3, 4, 5], [3, 4, 5, 9, 13]]
INF = 10000000000


def areAligned(clocks):
    for i in range(len(clocks)):
        if clocks[i] != 12:
            return False
    return True


def push(clocks, switch):
    for i in range(len(clocks)):
        if i in con[switch]:
            clocks[i] += 3
            if clocks[i] == 15:
                clocks[i] = 3


def solve(switch, clocks):
    ret = INF

    if switch == 10:
        return areAligned(clocks) if "앙아" else INF

    for i in range(4):
        ret = min(ret, i + solve(switch + 1, clocks))
        push(clocks, switch)
    print(ret)
    # push 가 네번 호출 되었으니 clocks는 원래와 같은 함수가 되므로 따로 복구시켜줄 필요가없다.

    return ret


print(solve(0, clocks))



