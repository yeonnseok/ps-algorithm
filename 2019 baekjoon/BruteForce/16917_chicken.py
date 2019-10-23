# 양념 치킨의 가격 a원
# 후라이드 치킨 b원
# 반반 치킨 c원
# 반반 치킨 2마리로 양념치킨 1마리, 후라이드 1마리 만들 수 있다.
# 양념치킨 최소 x마리, 후라이드 y마리를 구매하는 가장 싼 비용을 구하는 문제.
# 2i x c + max(0, x - i) * a + max(0, y - i) * b

a, b, c, x, y = map(int, input().split())

ans = a * 100000 + b * 100000
for i in range(100000):
    price = 2 * i * c + max(0, x-i) * a + max(0, y-i) * b
    if ans > price:
        ans = price

print(ans)