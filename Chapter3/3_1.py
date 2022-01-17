import time

print("[start]")
start_time = time.time() # 측정 시작

'''
### 예제 문제 화페 거슬러주기
n = 1260
count = 0

## 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types:  ## 화폐의 종류 만큼 for 문
    count += n // coin   ## 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    print("남은 돈인가? ", n)

print("동전의 개수 = ", count)
'''

'''
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
'''

''' 
## 곱하기 혹은 더하기 
data = input()

## 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    ## 두 수 중에 하나라도 '0' 혹은 '1' 인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else :
        result *= num
print(f"result = {result}")
'''

'''
## 큰 수의 법칙
## N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
## N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() ## 입력받은 수 정렬
first = data[n - 1] ## 가장 큰 수
second = data[n - 2] ## 두 번째로 가장 큰 수

## 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) *k
count += m % (k+1)

result = 0
result += (count) * first ## 가장 큰 수 더하기
result += (m - count) * second  ## 두 번째로 가장 큰 수 더 하기

print(f"최종 답안 출력 = {result}")
'''

'''
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
'''

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
