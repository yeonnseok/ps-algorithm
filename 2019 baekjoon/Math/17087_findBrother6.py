def findDistance(my, brothers):
    dist = []
    for i in range(len(brothers)):
        dist.append(abs(brothers[i] - my))
    return min(dist)


def main():
    src = list(map(int, input().split()))
    n, s = src[0], src[1]
    brothers = list(map(int, input().split()))
    print(findDistance(s, brothers))


main()