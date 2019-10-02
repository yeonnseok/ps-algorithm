
def normalize(num):
    num.append(0)
    for i in range(len(num)-1):
        if num[i] < 0:
            borrow = (abs(num[i]) + 9) // 10
            num[i+1] -= borrow
            num[i] += borrow * 10
        else:
            num[i+1] += num[i] // 10
            num[i] %= 10
    ans = []
    while num:
        ans.append(num.pop())
    return int(''.join(map(str, ans)))



c = [32, 52, 61, 60, 34, 16, 5]
print(normalize(c))