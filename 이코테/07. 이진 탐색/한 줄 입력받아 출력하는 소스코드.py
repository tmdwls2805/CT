import sys

# 하나의 문자열 데이터 입력받기
# readline() 후에 공백 문자를 제거하기위해 rstrip()을 반드시 써야함
input_data = sys.stdin.readline().rstrip()
# 입력받은 문자열 그대로 출력
print(input_data)