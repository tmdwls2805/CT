# N은 데이터의 개수, M은 더해지는 숫자의 개수, K는 연속될 수 있는 숫자
N, M, K = map(int, input().split())

# data 안에 들어갈 데이터 개수는 N개 이다.
data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]
print(first)
print(second)
result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)
