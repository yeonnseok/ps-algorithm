def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


def combination_calculate(src):
    n, m = src[0], src[1]
    return int(factorial(n) / (factorial(m) * factorial(n-m)))


def combination_zero_count(target):
    count = 0
    for i in reversed(range(len(target))):
        if target[i] == '0':
            count += 1
        else:
            return count


def main():
    src = list(map(int, input().split()))
    combi_result = combination_calculate(src)
    target = list(str(combi_result))
    print(combination_zero_count(target))


main()
