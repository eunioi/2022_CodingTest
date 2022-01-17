import time

print("[start]")
start_time = time.time() # 측정 시작

### 실전문제 1이 될 때까지
n, k = map(int, input().split())
print(f"n = {n}, k = {k}")
result = 0
while True :
    ## N이 K로 나누어 떨어지는 수가 될 떄까지 빼기
    target = (n // k) * k
    result += (n - target)
    print(f"result = {result}, 나누는 target = {target}")
    n = target
    ## N이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    ## k로 나눠라
    result += 1
    n //= k

## 마지막 남은 수에 대해서 1씩 빼기
result += (n - 1)
print(result)

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력