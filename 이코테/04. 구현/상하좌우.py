n = int(input())
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
moves = input().split()

# moves에 개수에 따라 어디로 이동하는지 찾는거니까 for문
for move in moves:
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # N X N 공간을 벗어날 경우에  x, y = nx, ny를 거치지 않고 for 문을 진행 (이거만 하면 끝임)
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x, y = nx, ny
print(x, y)