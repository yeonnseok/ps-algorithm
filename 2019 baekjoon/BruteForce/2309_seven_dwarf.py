def solve(src):
    for i in range(len(src)):
        for j in range(i + 1, len(src)):
            total = 0
            temp = []
            for k in range(len(src)):
                if src[k] == src[i] or src[k] == src[j]:
                    continue
                else:
                    total += src[k]
                    temp.append(src[k])
            if total == 100:
                temp.sort()
                return temp


def main():
    src = []
    for _ in range(9):
        src.append(int(input()))

    print(solve(src))

main()
