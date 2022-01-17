import time

print("[start] 4_3.py")
start_time = time.time() # 측정 시작
'''
왕실의 나이트
8x8 좌표 평면 수평으로 2-> 수직으로 1칸, 수직으로 2칸 -> 수평으로 1칸
가로 a~h, 세로 1~8 // 맵 밖으로 나갈 수 없음
'''

## 현재 나이트의 위치 받기
## input_data = input()
## row = int(input_data[1])

input_data = str('c1')
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) +1

## 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), ((-2, 1))]

## 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    ## 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    ## 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 9:
        result += 1
print(f"경우의 수 = {result}")
# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력