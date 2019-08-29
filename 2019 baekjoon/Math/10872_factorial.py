def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


def main():
    num = int(input())
    print(factorial(num))


main()

