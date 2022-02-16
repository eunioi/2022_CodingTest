'''
실전 문제 : 효율적인 화폐 구성

M원을 만들기 위한 최소한의 화폐 개수를 출력해라.
'''

print("정수 N, M을 입력 / 스페이스바로 구분")
n,m = map(int, input().split())
print("N개의 화폐 단위 정보 입력")
array = []
for i in range(n):
    array.append(int(input()))

## 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

## 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            ## print("(i-k)원을 만드는 방법이 존재하는 경우")
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print("최종적으로 M원을 만드는 방법이 없다 ! ")
else:
    print("M원을 만드는 최소한의 방법 = ", d[m])
