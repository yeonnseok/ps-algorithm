def makeOne(num):
    count = 0
    while num != 1:
        if num % 3 == 0:
            num /= 3
            count += 1
        elif num % 3 != 0:
            num -= 1
            count += 1
        elif num % 2 == 0:
            num /= 2
            count += 1
    return count


def main():
    num = int(input())
    print(makeOne(num))

main()