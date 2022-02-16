'''
실전 문제 : 바닥 공사
1x2, 2x1, 2x2 덮게를 이용해 채울거야

다이나믹 프로그래밍 기초 예제 : 타일링 문제 유형

'''
print("정수 N을 입력받기")
n = int(input())

## 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

## 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1]+2 *d[i-2]) % 796796

print(f"바닥을 채우는 경우의 수는 {d[n]} 개다.")