def solve(n, m, src):
    # 현재 채널은 100번
    # 100에서
    ll = list(str(n))
    count = 0
    temp = []
    if n - 100 < len(ll):
        count = n - 100
    else:
        for i in range(len(ll)):
            if int(ll[i]) in src:
                idx = 1
                while int(ll[i]) - idx in src:
                    idx += 1
                if int(ll[i]) - idx >= 0:
                    temp.append(str(int(ll[i]) - idx))
                elif int(ll[i]) - idx < 0:
                    temp.append(str(int(ll[i]) + idx))
            else:
                temp.append(ll[i])

        count += len(ll)
        count += abs((n - int(''.join(temp))))

    return count


def main():
    n = int(input())
    m = int(input())
    src = list(map(int, input().split()))
    print(solve(n, m, src))


main()
