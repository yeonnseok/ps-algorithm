k = int(input())
for _ in range(k):
    n = int(input())


    def one_two_three_adding(goal, ssum):
        if ssum > goal:  # 불가능
            return 0
        if ssum == goal:  # 정답
            return 1

        now = 0
        for i in range(1, 4):
            now += one_two_three_adding(goal, ssum + i)
        return now

    print(one_two_three_adding(n, 0))

