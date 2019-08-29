def to_tenjin(jins, src):
    n = 0
    ans = 0
    for i in reversed(range(len(src))):
        ans += src[i] * (jins[0] ** n)
        n += 1
    return ans


def from_tenjin(jins, tenjins):
    # 여기선 src가 10진수
    ans = []
    while tenjins > 1:
        ans.insert(0, tenjins % jins[1])
        tenjins //= jins[1]

    return ans


def base_conversion(jins, src):
    tenjins = to_tenjin(jins, src)
    return from_tenjin(jins, tenjins)


def main():
    jins = list(map(int, input().split()))
    numOfJari = int(input())
    src = list(map(int, input().split()))
    print(base_conversion(jins, src))


main()

