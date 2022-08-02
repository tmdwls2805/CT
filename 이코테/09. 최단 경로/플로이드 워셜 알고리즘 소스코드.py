# 플로이드 워셜은 모든 경로의 최단 경로 경우의 수를 구하는 알고리즘임

INF = int(1e9)

# 노드 및 간선의 개수
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 값은 0으로 초기화

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# 각 간선에 대한 정보를 입력 받아, 그 값을 초기화
