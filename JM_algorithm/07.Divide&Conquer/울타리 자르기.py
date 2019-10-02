

h = [7, 1, 5, 9, 6, 7, 3]


# def bruteForce(h):
#     ret = 0
#     n = len(h)
#     for i in range(n):
#         minHeight = h[i]
#         for j in range(i, n):
#             minHeight = min(minHeight, h[j])
#             ret = max(ret, (j - i + 1) * minHeight)
#     return ret
#
# print(bruteForce(h))


def divideConquer(left, right):
    if left == right:
        return h[left]
    mid = (left + right) // 2
    ret = max(divideConquer(left, mid), divideConquer(mid+1, right))

    lo = mid
    hi = mid + 1
    height = min(h[lo], h[hi])
    ret = max(ret, height * 2)

    while left < lo or hi < right:
        if hi < right and (lo == left or h[lo-1] < h[hi+1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1
            height = min(height, h[lo])

        ret = max(ret, height * (hi - lo + 1))
    return ret

