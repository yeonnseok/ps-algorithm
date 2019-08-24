def findNGF(arr, idx):
    for i in range(idx, len(arr)):
        if arr.count(arr[idx-1]) < arr.count(arr[i]):
            return arr[i]
    return -1


def main():
    numOfArr = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for idx in range(1, numOfArr+1):
        ans.append(findNGF(arr, idx))
    print(ans)


main()
