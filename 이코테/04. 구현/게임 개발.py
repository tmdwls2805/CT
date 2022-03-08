# 꽤나 복잡한 문제임
# 맵 크기 정의
n, m = map(int, input().split())


# for 문에서의 _는 실제로 사용되지 않기 때문에 언더바 '_'를 사용함
# 인터프리터에 값을 저장하거나
# 사용하지 않을 떄 사용
# 아래와 같은 경우는 값을 저장하기 위해서 사용되는 것 같음
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화한다.'
# (x, y)는 현재 좌표, (nx, ny)는 이동할 좌표, (dx, dy)는 동서남북
# 방문한 지역을 체크하기 위해서 맵을 0으로 초기화 시킴
d = [[0] * m for _ in range(n)]

# 캐릭터 위치 지정 및 바라보는 방향 입력
x, y, direction = map(int, input().split())
# 현재 좌표는 방문 위치로 저장
d[x][y] = 1

# 전체 맵 정보 입력으로 받기
# 맵이 육지와 바다 무엇으로 이루어져 있는지 입력 받음
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def turn_left():
    # direction은 함수 밖에서도 사용할 것이기 떄문에 전역변수로 취함
    global direction
    # 왼쪽으로 도니까 -1을 해줘야겠죠. 아래 참고
    direction -= 1
    # 북 동 남 서  0 1 2 3 순이기 떄문에 0에서 왼쪽으로 갈 경우 서쪽이여서 3으로 초기화
    if direction == -1:
        direction = 3

# 방문 칸 수
count = 1
# 회전한 횟수
turn_time = 0

# 이 문제는 반복하는 횟수가 정해져 있지 않기 때문에 while문을 통해 무한루프를 탐
while True:
    # 현재 바라보고 있는 방향에서 왼쪽으로 (전역변수가 결과값으로 튀어나옴 : direction)
    turn_left()
    # 이동할 좌표를 확인하기 위해 기존 좌표에 바라보는 좌표를 더함
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 방문하지 않은 곳이고, 방문하지 않은 곳이 육지 라면 ....
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 방문한 지역을 체크함
        d[nx][ny] = 1
        # 방문할 수 있는 지역으로 이동했기 때문에 캐릭터에 대한 x, y 좌표를 이동시킨다.
        x = nx
        y = ny
        # 새로 방문한 지역 수를 카운트 한다.
        count += 1
        # 만약에 방문할 수 있는 곳이라면 회전 횟수를 초기화 한다.
        turn_time = 0
        # 계속 진행 (while문 처음으로)
        continue
    # 방문할 수 없다면 회전만 진행한다. 그리고 다시 while 문 첫번째로 가서 진행
    else:
        turn_time += 1
    # 네 방향을 모두 갈 수 없는 상황이라면
    if turn_time == 4:
        #바라보고 있는 방향에서 뒤로 이동함; 그렇게 하기 위해서 dx의 direction 좌표에 -를 취하게 되면 바라보는 방향의 반대 방향이 됨
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 현재 바라보고 있는 방향에서 뒤로 이동해야하는데
        # 뒤로 이동하는 방향에 있는 칸이 육지라면
        if array[nx][ny] == 0:
            # 현재 캐릭터의 좌표를 뒤로 이동시키고, 현재 좌표를 저장함
            x = nx
            y = ny
        # 육지가 아니라면
        else:
            # 그대로 종료
            break
        # 뒤로 이동한 후 초기화하지 않으면 turn_time이 4를 초과해서 if문에 걸리지 않아 무한루프를 돌게 됨
        # 무한루프를 타면 결과 값은 나오지 않겠죠
        turn_time = 0
# 방문한 지역 수를 출력
print(count)