# 각 학생의 점수를 계산하는 함수
def score_calculate(student, answers):
    score = 0
    for i in range(len(student)):
        if answers[i] == student[i]:
            score += 1
    return score


def solution(answers):
    answer = []
    n = len(answers)

    # 문제 갯수에 맞는 각 학생들의 답안
    st1 = [1, 2, 3, 4, 5]
    st1 = st1 * (n // 5) + st1[:n % 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st2 = st2 * (n // 8) + st2[:n % 8]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    st3 = st3 * (n // 10) + st3[:n % 10]

    # 점수 계산 함수를 통해 각 학생들의 점수를 배열에 저장
    scores = []
    scores.append(score_calculate(st1, answers))
    scores.append(score_calculate(st2, answers))
    scores.append(score_calculate(st3, answers))

    # 배열을 돌면서 최대값과 일치하는 점수의 인덱스를 정답배열에 저장
    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i + 1)
    return answer