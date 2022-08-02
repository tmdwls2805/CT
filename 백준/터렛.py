# 두 원의 중심과 반지름을 입력했을 때, 두 원 사이의 접점의 개수를 구하는 문제
# 원의 중심 좌표 (x, y) 2쌍이 주어질 때, 두 좌표 사이의 거리를 구하는 공식을 알아야함

import math
# T는 테스트 케이스의 개수이다.
T = int(input())

for _ in range(T):
    # 입력 값
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    # 두 원의 중심 사이의 거리
    dis = math.sqrt((x1 - x2)**2 + (y1-y2)**2)

    if dis == 0: # 두 원의 중심이 같을 경우
        if r1 == r2: # 두 원의 크기가 같아 겹치는 경우
            print(-1) # 무한대 이므로 -1
        else:       # 한 원이 다른 원 안에 들어가 있는 경우
            print(0)
    else:
        if r1+r2 == dis or abs(r2-r1) == dis: # 두 원의 중심이 다를 경우
            print(1)
        elif((abs(r1 - r2) < dis) and (dis < (r1 + r2))):
            print(2)
        else:
            print(0)
