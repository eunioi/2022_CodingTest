import time

print("[start] ex_DFS.py")
start_time = time.time() # 측정 시작

'''
BFS : Breadth-First Search,  너비 우선 탐색 : 가까운 노드부터 우선적으로 탐색하는 알고리즘
큐 자료구조를 이용, 방문 기준은 번호가 낮은 인접 노드부터 합니다.
'''
from collections import deque

## BFS 메서드 정의
def bfs(graph, start, visited):
    ## 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    ## 현재 노드를 방문 처리
    visited[start] = True
    ## 큐가 빌때까지 반복
    while queue:
        ## 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end = ' ')
        ## 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

## 각 노트가 방문된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

## 각 노트가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

## 정의된 DFS 함수 호출
bfs(graph, 1, visited)



# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
