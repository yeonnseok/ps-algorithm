def getGCD(a, b):
    if a % b == 0 :
        return b
    return getGCD(b, a%b)


def GCD_ADD(nums):
    sum = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum += getGCD(nums[i], nums[j])
    return sum


def main():
    numOfCase = int(input())
    for i in range(numOfCase):
        src = list(map(int, input().split()))
        n = src[0]
        nums = src[1:]
        if n != len(nums):
            return -1
        print(GCD_ADD(nums))


main()