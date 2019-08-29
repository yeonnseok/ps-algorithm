def minusbinary(ans, num):
    if num == 0:
        return
    if num % -2 == 0:
        ans.insert(0, "0")
        minusbinary(ans, num/-2)
    else:
        ans.insert(0, "1")
        minusbinary(ans, (num - 1) / -2)
    return ''.join(ans)


def main():
    num = int(input())
    ans = []
    print(minusbinary(ans, num))


main()
