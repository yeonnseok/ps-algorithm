def findNGE(arr, idx):
    for i in range(idx, len(arr)):
        if arr[idx-1] < arr[i]:
            return arr[i]
    return -1


def main():
    numOfArr = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for idx in range(1, numOfArr+1):
        ans.append(findNGE(arr, idx))
    print(ans)


main()