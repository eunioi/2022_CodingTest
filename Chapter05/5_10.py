import time

print("[start] 음료수 얼려 먹기")
start_time = time.time() # 측정 시작

'''
첫번째 줄에 얼음 틀의 세로 길이 N, 가로길이 M 이 주어짐(1 <= N, N <= 1,000)
두번째 줄부터 N+1번째 줄까지 얼음틀의 형태가 주어짐
이때 구멍이 뚫려있는 부분은 0, 막혀있는 부분은 1
한번에 만들 수 있는 아이스크림의 개수를 구하시오  
'''
def dfs(x, y):
    ## 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    ## 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        ## 해당 노드 방문 처리
        graph[x][y] = 1
        ## 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

## N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

## 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

## 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        ## 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(f"최종 한번에 만들 수 있는 아이스크림의 개수 = {result}")

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("\n[time] ", end_time - start_time) # 수행 시간 출력
