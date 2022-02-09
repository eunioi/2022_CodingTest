print("[start] 실전 문제 위에서 아래로")

'''
첫번째 줄에 수열에 속해있는 수의 개수 N이 주어진다. (1<= N <= 500)
둘째 줄 부터 N+1번째 줄까지 N개의 수가 입력된다.
수의 범위는 1이상 100,000 이하의 자연수이다. 
'''

## N을 입력받기
n = int(input())

## N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

## 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse = True)

## 정렬이 수행된 결과를 출력
for i in array:
    print(i, end= ' ') 
