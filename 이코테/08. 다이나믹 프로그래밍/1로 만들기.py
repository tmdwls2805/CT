# 나눌 입력값
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        # 점화식 끝에 1을 더하는 이유는 호출 횟수를 구해야 하기 떄문이다.
        # 1을 뺸 값은 거의 값이 크기 때문에 나눈 값들과 비교한다.ㄴ
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    print(d[i])
print(d[x])