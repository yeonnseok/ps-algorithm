def soinsu(num):
    for pn in range(2, num+1):
        t_count = 0
        for idx in range(2, pn):
            if pn % idx == 0:
                t_count += 1
        if t_count == 0:
            while num % pn == 0:
                print(pn)
                num /= pn


def main():
    num = int(input())
    soinsu(num)


main()
