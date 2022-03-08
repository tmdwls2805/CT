#
# n, k = map(int, input().split())
# result = 0
#
# while n >= k:
#     while n % k != 0:
#         n = n - 1
#         result += 1
#     n = n // k
#     result += 1
#
# result += n-1
# print(result)

## 위와 같이 사용하면 상수의 시간 복잡도를 갖고 진행함

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += n - target
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)

## 위와 같이 사용하면 log의 시간 복잡도를 갖고 진행할 수 있다.
