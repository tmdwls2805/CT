input_data = input()
row = int(input_data[1])
# 아스키코드 ord()함수를 이용해서 문자열을 숫자로 변경한 후 에 진행
# 왜냐? 밑에 부분에서 그 지역으로 갈 수 있을지 없을지 더 해서 구해야하니까 이놈아
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (-1, 2), (1, 2)]

result = 0
# 이동할 수 있는 경로의 경우의 수만 생각하면되기 떄문에 for문을 사용함
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    ## 아래와 같은 조건을 모두 만족할 시에는 말이 움직일 수 있기 때문에 더함
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)