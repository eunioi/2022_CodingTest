'''
다이나믹 프로그래밍을 사용하는 조건
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

피보나치 수열은 위의 조건을 만족하는 대표 문제.

Memoization 기법을 사용해서 해결하자.
    - 다이나믹 프로그래밍을 구현하는 방법 중 한 종류
    - 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법을 의미
    - 다른말로 캐싱(Caching) 이라고 부름.
'''
print("피보나치 수열 소스코드 (재귀적)")
print("한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화")
d = [0] * 100

## 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
## 탑다운(Top-Diwn)방식 : 큰 문제를 해결하기 위해 작은 문제를 호출하는 방법
def fibo(x):
    ## 종료 조건 (1 혹은 2 일 때 1을 반환)
    if x == 1 or x == 2:
        print(f"종료 조건 1 or 2, x = {x}, d[x] = {d[x]}")
        return 1
    ## 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        print(f"계산 한 적 있는 문제라면, x = {x}, d[x] = {d[x]}")
        return d[x]
    ## 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

cnt = 99
print(f"x = {cnt}, {cnt} 번째 피보나치 수열 값은 {fibo(cnt)}")
