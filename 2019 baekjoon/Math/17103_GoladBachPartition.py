def is_primeNumber(num):
    if num != 1:
        t_count = 0
        for idx in range(2, num):
            if num % idx == 0:
                t_count += 1
        if t_count == 0:
            return True
        else:
            return False
    else:
        return False


def under_primeNumber(num):
    arr = []
    for i in range(1, num + 1):
        if is_primeNumber(i):
            arr.append(i)
    return arr


def devide_two_primeNumber(num):
    pn = under_primeNumber(num)
    ans_count = 0
    for i in range(len(pn)):
        for j in reversed(range(i, len(pn))):
            if pn[i] + pn[j] == num:
                ans_count += 1

    return ans_count


def main():
    numOfCase = int(input())
    for i in range(numOfCase):
        num = int(input())
        print(devide_two_primeNumber(num))


main()

