# 이진 탐색 코드 구현 ( 재귀 함수 사용 )
def binary_search(array, target, start, end):
    # start 값이 end 보다 크면 None을 반환
    if start > end:
        return None
    mid = (start+end) // 2

    # 찾은 경우 중감점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

# n(원소 개수)와 target(찾고자 하는 문자열) 입력 받기
n, target = map(int, input().split())
# 전체 원소 입력 받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)