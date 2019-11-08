def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort(key=lambda x: len(x))
    for i in range(n):
        for j in range(i + 1, n):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return answer