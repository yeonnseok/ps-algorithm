def next_permutation(src):
    n = len(src)
    i = n - 1
    while src[i-1] >= src[i]:
        i -= 1
    if i <= 0: return -1

    j = n - 1
    while src[i-1] >= src[j]:
        j -= 1
    src[i-1], src[j] = src[j], src[i-1]

    j = n - 1
    while i < j:
        src[i], src[j] = src[j], src[i]
        i += 1
        j -= 1

    return True


def solve(n, src):
    ans = 0
    src.sort()  # 모든 순열을 순회할 때는 정렬 필수!

    for i in range(n - 1):
        ans += abs(src[i] - src[i + 1])

    while next_permutation(src) != -1:
        temp = 0
        for i in range(n - 1):
            temp += abs(src[i] - src[i+1])

        if ans < temp:
            ans = temp

    return ans


def main():
    n = int(input())
    src = list(map(int, input().split()))
    print(solve(n, src))


main()
