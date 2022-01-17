import time

print("[start]")
start_time = time.time() # 측정 시작

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


# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력