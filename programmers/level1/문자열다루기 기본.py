def solution(s):
    n = len(s)
    if n == 4 or n == 6:
        try:
            int(s)
            return True
        except:
            return False
    return False