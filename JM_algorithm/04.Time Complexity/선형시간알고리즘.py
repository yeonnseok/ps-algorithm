# 길이가 n인 실수 배열 a가 주어질 때, 각 위치에서의 m-이동 평균값을 구하여라

a = [3.5, 3.6, 4, 6, 7, 10, 11, 15, 16, 20, 26, 24, 26, 26.2, 25.4, 26, 29, 30, 40, 41, 42.6, 44, 43, 47, 49.5, 53, 53, 56]


def movingAverage2(a, m):
    n = len(a)
    ret = []
    partialSum = 0
    for i in range(m-1):
        partialSum += a[i]

    for i in range(m-1, n):
        partialSum += a[i]
        ret.append(partialSum / m)
        partialSum -= a[i-m+1]
    return ret

print(movingAverage2(a, 3))

