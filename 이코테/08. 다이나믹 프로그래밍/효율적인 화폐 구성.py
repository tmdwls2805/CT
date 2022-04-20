# n은 화폐의 종류, m은 만들 금액
n, m = map(int, input().split())

# 화폐 종류
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)
            print('중간값 : ', d[j])
if d[m] == 10001:
    print(-1)
else:
    print(d[m])