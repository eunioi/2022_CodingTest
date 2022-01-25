import time

print("[start] 4_2.py")
start_time = time.time() # 측정 시작
'''
시각
N이 입력되면 00시 00분 00초 까지 N시 59분 59초 까지 3을 포함하는 경우의 수를 구하라
3중 for문이 제일 best 래
'''
## H 입력받기
## h = int(input())
h = int(10)

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            ## 매 시각 안에 3이 포함되면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(f"경우의 수 = {count}")
# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("종료 time:", end_time - start_time) # 수행 시간 출력
