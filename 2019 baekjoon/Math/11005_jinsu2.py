def jinsu(ans, target, jin):
    if target == 0:
        return
    while target > 1:
        if target % jin < 10:
            ans.insert(0, target % jin)
        elif target % jin >= 10:
            ans.insert(0, chr(int(target % jin) + 55))
        target /= jin
    return ''.join(ans)


def main():
    num = list(map(int, input().split()))
    ans = []
    print(jinsu(ans, num[0], num[1]))


main()
