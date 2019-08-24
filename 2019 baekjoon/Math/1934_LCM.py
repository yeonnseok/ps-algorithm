# 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
# 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다.
# 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.


def findLCM(src):
    n1, n2 = src[0], src[1]
    LCM = 0
    idx = max(n1, n2)
    while LCM == 0:
        if idx % n1 == 0 and idx % n2 == 0:
            LCM = idx
        idx += 1
    return LCM


def main():
    numOfCase = int(input())
    for i in range(numOfCase):
        src = list(map(int, input().split()))
        print(findLCM(src))


main()