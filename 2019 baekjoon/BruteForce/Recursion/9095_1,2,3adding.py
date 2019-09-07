def solve(summ, goal):
    if summ > goal:  # 불가능한 경우
        return 0
    if summ == goal:  # 정답을 찾은 경우
        return 1
    now = 0
    for i in range(1, 4):  # 다음 재귀함수 호출
        now += solve(summ + i, goal)
    return now


def main():
    n = int(input())
    for _ in range(n):
        goal = int(input())
        summ = 0
        print(solve(summ, goal))


main()
