N = int(input())

array = []
for i in range(N):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in range(len(array)):
    print(array[i], end=' ')