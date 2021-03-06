'''
보텀업(Bottom-Up) : 단순히 반복문을 이용하여 작성, 작은 문제부터 답을 도출하는 방법

피보나치 수열 소스코드(반복적)
'''

'''
탑다운(메모이제이션) 방식 - 하향식
보텀업 방식 - 상향식

다이나믹 프로그래밍의 전형적인 형태는 '보텀업 방식'
DP 테이블 : 보텀업 방식에서 사용되는 결고 저장용 리스트
메모이제이션 : 탑다운 방식에 국한되어 사용되는 표현

다이나믹 프로그래밍 문제는 대체로 간단한 형댈도 추렞됨.
< 문제를 푸는 단계 >
1. 다이나믹 프로그래밍 유형을 파악하는 것
메모이제이션을 적용할 수 있으면 코드를 개선하는 방법도 좋은 아이디어.
재귀 함수를 작성한 후 -> 메모이제이션 기법을 적용해 소스코드를 구정하는 것도 좋음.

재귀함수로 구현하는 방법(탑다운 방식) 보다는 보텀업 방식을 권장함.
'''

## 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

## 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 3

## 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]

print(f"n = {n}, d[{n}] = {d[n]}")
