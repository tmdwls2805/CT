n = int(input())

array = []
# 데이터를 key, value 값으로 list에 저장함
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# lambda 식으로 키 값을 기준으로 정렬함
array = sorted(array, key=lambda student: student[1])

# 위에서 정렬된 값을 기준으로 value 값을 뽑아냄 (오름차순)
for student in array:
    print(student[0], end=' ')
