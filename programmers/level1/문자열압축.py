def solution(s):
    answer = 0
    cache = [100000] * 1001
    n = len(s)

    for i in range(1, n + 1):
        temp = []
        for j in range(0, n, i):
            temp.append(s[j: j + i])

        cnt = 1
        j = 1
        ans = ''
        while j <= len(temp):
            if j == len(temp):
                if cnt != 1:
                    ans += '%d' % cnt
                ans += temp[j - 1]

            elif temp[j - 1] == temp[j]:
                cnt += 1

            else:
                if cnt != 1:
                    ans += '%d' % cnt
                ans += temp[j - 1]
                cnt = 1
            j += 1
        cache[i] = len(ans)
    answer = min(cache)
    return answer