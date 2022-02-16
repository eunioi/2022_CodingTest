'''
다이나믹 프로그램 : 한 번 계산한 문제는 다시 계산하지 않도록 하는 알고리즘
1. 중복되는 연산을 줄이자.
    -> 횽ㄹ적인 알고리즘 작성

대표적인 예시
피보나치 수열 : 이전 두 항의 합을 현재의 항으로 설정
n1, n2 = 1로 설정되어야한다.
'''

'''
피보나치 함수 소스코드
'''
## 피보나치 함수 (Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        print(f"x = {x}, 1을 반환합니다.")
        return 1
    return fibo(x - 1) + fibo(x-2)

count = 9
print(f"x = {count}, {count}번째 값 = {fibo(count)}")