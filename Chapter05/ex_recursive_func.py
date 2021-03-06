import time

print("[start] ex_recursive_func.py")
start_time = time.time() # 측정 시작

'''
재귀 함수(Recursive Funcion) : 자기 자신을 다시 호출하는 함수
팩토리얼 구현 예제
n! = 1 x 2 x 3 x ... x (n-1) x n
'''
## 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    ## 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

## 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  ## n이 1 이하인 경우 1을 반환
        return 1
    ## n! = n * (n-1)! 를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

## 각각 방식으로 구현한 n! 출력 n = 5
print(f"반복적으로 구현 : {factorial_iterative(5)}")
print(f"재귀적으로 구현 : {factorial_recursive(5)}")
# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력 
