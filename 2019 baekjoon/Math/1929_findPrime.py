# M이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.


def solve(src):
    m, n = src[0], src[1]
    ans = []
    for num in range(m, n + 1):
        prime = True
        if num < 2:
            prime = False
        else:
            for t in range(2, num):
                if num % t == 0:
                    prime = False
        if prime is True:
            ans.append(num)
    return ans


def main():
    src = list(map(int, input().split()))
    print(solve(src))


main()
