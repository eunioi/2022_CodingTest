import time

print("[start]")
start_time = time.time() # 측정 시작

## 숫자 카드 게임
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    print(f"입력받은 data = {data}")
    min_value = min(data)
    print(f"현재 줄에서 가장 작은 수 찾기 = {min_value}")
    result = max(result, min_value)
    print(f"가장 작은 수 들 중에서 가장 큰 수 찾기 = {result}")

print(f"최종 답안 출력 = {result}")

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력