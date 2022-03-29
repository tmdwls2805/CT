# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)


print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))
# 둘의 결과는 동일하지만
# 반복문 대신 재귀 함수를 사용하면 코드가 더 간결하다.
# 점화식 = 재귀식 에서는 종료 조건을 입력해야 무한 반복을 피할 수 있음
