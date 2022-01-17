import time

print("[start] 4_1.py")
start_time = time.time() # 측정 시작
'''
상화 좌우 ? 
NxN 크기의 정사각형 공간이 있다. 
시작좌표는 (1, 1), 여행가가 움직임.
움직임은 L, R, U, D이고, 지도를 벗어나면 무시한다. 
1<=N<=100 // 이동할 계획서가 주어짐.
'''

## N을 입력받기
## n = int(input())

## 설정함
n = int(13)
x,y = 1, 1

## plans 입력 받기
#plans = input().split()
#print(plans, type(plans))

## 설정함
plans = list(['U', 'U', 'R', 'R', 'L', 'L', 'U', 'U', 'R', 'R', 'D', 'D', 'L'])

## L , R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

## 이동 계획을 하나씩 확인
for plan in plans:
    ## 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    ## 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    ## 이동 수행
    x, y = nx, ny
    ##print(f"plan = {plan}, 이동 좌표 = ({x}, {y})")
print(f"마지막 좌표 (x, y) = ({x},{y})")

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
