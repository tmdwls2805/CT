# n, m = map(int, input().split())
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_data = min(data)
#     result = max(result, min_data)
# print(result)

## 이중 for문으로 가능

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_data = 10001
    for a in data:
        min_data = min(min_data, a)
    result = max(result, min_data)
print(result)