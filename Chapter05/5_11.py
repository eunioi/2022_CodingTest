import time
from collections import deque

print("[start] 미로 탈출")
start_time = time.time() # 측정 시작

'''
N x M 크기의 직사각형 형태의 미로에 갇혔다.
두 정수 N, M(4 <= N, M <= 200) 이 주어진다. 
다음 N개의 줄에는 각각 M개의 정수(0 or 1)로 미로의 정보가 주어진다.
시작칸과 마지막칸은 항상 1이다.
첫째 줄에 최소 이동 칸의 개수를 출력하시오.
'''

'''
해결 방안 
BFS 사용. 모든 노드의 최단 거리 값을 기록하면 해결 할 수 있다.
값을 올리는 식으로 해결 하면 할 수 있다.
'''

## BFS 소스 코드 구현
def bfs(x, y):
    ## 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    ## 현재 위치에서 4가지 방향으로의 위치 확인
    while queue:
        x, y = queue.popleft()
        ## 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ## 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            ## 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            ## 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    ## 가장 오른쪽 아래까지의 최단 거리 반환
    print(f"최종 graph = {graph}")
    return graph[n-1][m-1]

## N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

## 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

## 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

## BFS를 수행한 결과 출력
print(f"미로 탈출 최소 거리 : {bfs(0, 0)}")

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("\n[time] ", end_time - start_time) # 수행 시간 출력
