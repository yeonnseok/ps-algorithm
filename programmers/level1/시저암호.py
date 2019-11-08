def solution(s, n):
    answer = ''

    for ch in s:
        if ch == " ":
            answer += ch
        else:
            if 65 <= ord(ch) <= 90:
                answer += chr(((ord(ch) + n) - ord('A')) % 26 + ord('A'))
            else:
                answer += chr(((ord(ch) + n) - ord('a')) % 26 + ord('a'))
    return answer