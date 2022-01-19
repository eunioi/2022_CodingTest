import time

print("[start] ex_DFS.py")
start_time = time.time() # 측정 시작

'''
DFS : Depth-First Search, 깊은 부분을 우선적으로 탐색하는 알고리즘
스택 자료구조 or 재귀함수를 이용, 방문 기준은 번호가 낮은 인접 노드부터 합니다.
'''

## DFS 메서드 정의
def dfs(graph, v, visited):
    ## 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    ## 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
## 각 노트가 방문된 정보를 표현 (2차원 리스트)
## 이게 어떻게 해석 될 수 있냐면,
## 0번째 인덱스는 무시하고
## 1번이랑 연결된 것 = 2, 3, 8
## 2번이랑 연결된 것 = 1, 7 이런식으로 인섹스가 각 숫자라고 생각
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
dfs(graph, 1, visited)



# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력