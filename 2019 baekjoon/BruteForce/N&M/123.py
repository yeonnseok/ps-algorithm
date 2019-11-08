def recursive(numbers, n, index, cur, target):
    global ans
    if index == n:
        if cur == target:
            ans += 1
        return

    recursive(numbers, n, index+1, cur+numbers[index], target)
    recursive(numbers, n, index+1, cur-numbers[index], target)


numbers = [1, 1, 1, 1, 1]
target = 3
ans = 0
n = len(numbers)
recursive(numbers, n, 0, 0, target)
print(ans)
