# M이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.


def solve(src):
    m, n = src[0], src[1]
    ans = []
    for num in range(m, n + 1):
        if num > 1:
            t_count = 0
            for j in range(2, num):
                if num % j == 0:
                    t_count += 1
            if t_count == 0:
                ans.append(num)
    return ans


def main():
    src = list(map(int, input().split()))
    list(map(print, solve(src)))


main()