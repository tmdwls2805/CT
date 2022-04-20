# n 떡의 개수, m 손님이 원하는 떡의 길이
n, m = list(map(int, input().split(' ')))
# 떡의 각각의 길이
array = list(map(int, input().split()))

# m의 길이 떡을 얻기 위해서 절단기에서 설정할 수 있는 최대 길이
# 절달기의 높이는 h

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 떡의 길이가 mid 보다 길면 빼기를 진행해서 잘린 길이만큼 저장한다.
        if x > mid:
            total += x - mid
    print(total)
    # 만약 잘린 떡의 길이가 m(손님의 원하는 떡의 길이)보다 부족하다면 왼쪽으로 이동한다.
    if total < m :
        end = mid-1
    # 만약 떡의 잘린 길이가 충분하다면 덜 자른다 (오른쪽으로 이동)
    else:
        result = mid
        start = mid + 1

print(result)