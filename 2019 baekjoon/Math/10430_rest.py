def four_rest(src):
    #src는 정수 리스트
    ans = []
    ans.append((src[0] + src[1]) % src[2])
    ans.append(((src[0] % src[2]) + (src[1] % src[2])) % src[2])
    ans.append((src[0] * src[1]) % src[2])
    ans.append(((src[0] % src[2]) * (src[1] % src[2])) % src[2])
    return ans


def main():
    src = list(map(int, input().split()))
    list(map(print, four_rest(src)))

main()