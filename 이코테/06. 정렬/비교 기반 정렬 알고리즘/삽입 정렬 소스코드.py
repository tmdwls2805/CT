array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # i번째 원소부터 첫 번째 원소까지 -1씩 줄어들면서 반복
    for j in range(i, 0, -1):
        # 한칸씩 왼쪽으로 이동
        if array[j] < array[j - 1]:
            # 왼쪽에 있는 원소가 현재 원소보다 작으면 위치 스와프~
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)