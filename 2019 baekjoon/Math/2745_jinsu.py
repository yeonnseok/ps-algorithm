def jinsu(target, jin):
    if target == 0:
        return

    ans = 0
    n = 0
    for i in reversed(range(len(target))):
        if target[i].isdigit():
            ans += target[i] * (jin ** n)
        else:
            target[i] = ord(target[i]) - 55
            ans += target[i] * (jin ** n)
        n += 1
    return ans


def main():
    src = input().split()
    print(jinsu(list(src[0]), int(src[1])))


main()
