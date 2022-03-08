# stack filo임
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
# pop()을 그냥 사용하면 list의 오른쪽 value 부터 삭제함
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) 
# ::를 두개 붙이면 리버스 출력