def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(99))

# 다음과 같이 작성하면 n이 커질수록 수행시간이 기하급수적을 늘어남
# 이것을 해결하기 위해 메모이제이션을 사용띠