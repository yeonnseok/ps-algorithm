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
    for i in range(len(pn)):
        for j in range(i + 1, len(pn)):
            if pn[i] + pn[j] == num:
                return pn[i], pn[j]


def main():
    while 1:
        num = int(input())
        if num == 0:
            break
        else:
            one, two = devide_two_primeNumber(num)
            print(num, ' = ', one, ' + ', two)


main()

