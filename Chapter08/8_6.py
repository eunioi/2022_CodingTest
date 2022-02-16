'''
실전문제 : 개미 전사
정찰병에서 들키기 않고 식량 창고를 약탈하기 위해서는 최소 한 칸 이상 떨어진 식량창고를 약탈해야한다.
일직선상일 때 최대한 많은 식량을 얻기를 원한다.

보텀업 방식의 풀이로 진행
'''
print("정수 N 입력 하라.")
n = int(input())

print("모든 식량 정보 입력받기 띄어쓰기로.")
array = list(map(int, input().split()))

## 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

## 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = array[0]
print("d[0] = ", d[0])
## array[0], array[1] 중에서 더 큰 수를 d[1] 에 넣는다.
d[1] = max(array[0], array[1])
print("d[1] = ", d[1])

## 2부터 n까지 for문 돈다.
for i in range(2, n):
    ##
    d[i] = max(d[i-1], d[i-2] + array[i])
    print(f"\n\nd[{i}] = {d[i]}, d[{i-1}] = {d[i-1]}, d[{i-2}] = {d[i-2]},"
          f"\narray[{i}] = {array[i]}, d[{i-2}]+array[{i}] = {d[i-2]+array[i]}")
print(f"가장 큰 값은 {d[n-1]}")
