# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.


def GCF_LCM(src):
    n1, n2 = src[0], src[1]
    GCF = 0
    LCM = 0
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
           GCF = i

    t = max(n1, n2)
    while LCM == 0:
        if t % n1 == 0 and t % n2 == 0:
           LCM = t
        t += 1
    return (GCF, LCM)


def main():
    src = list(map(int, input().split()))
    list(map(print, GCF_LCM(src)))


main()
