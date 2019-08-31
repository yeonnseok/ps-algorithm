def solve(src):
    E, S, M = src[0], src[1], src[2]
    yr = 1
    while 1:
        if ((yr-E) % 15 == 0) and ((yr-S) % 28 == 0) and ((yr-M) % 19 == 0):
            break
        yr += 1
    return yr


def main():
    src = list(map(int, input().split()))
    print(solve(src))


main()
