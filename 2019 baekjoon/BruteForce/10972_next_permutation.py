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
    return ' '.join(map(str, src))


def main():
    src = list(map(int, input().split()))
    print(next_permutation(src))


main()
