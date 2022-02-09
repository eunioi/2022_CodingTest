'''
파라메트릭 서치(Parametric Search)
- 최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법.
- 예시 : 특정한 조건을 만족하는 가장 알맞은 값을 찾는 최적화 문제
- 이진 탐색을 이용하여 해결 할 수 있음

실전 문제 3. 떡볶이 떡 만들기

입력 조건
1. 첫재 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
    (1 <= N <= 1,000,000, 1<= M <= 2,000,000,000)
2. 둘째 줄에는 떡의 개별 높이가 주어짐.
    떡 높이의 총합은 항상 M이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
3. 절단기(N)의 높이는 0~10억

출력 조건
- 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력

Point
' 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야한다. '
'''
print("떡의 개수(N)와 요청한 떡의 길이(M)을 입력")
n, m = list(map(int, input().split(' ')))
print("각 떡의 개별 높이 정보를 입력")
array = list(map(int, input().split()))

## 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

## 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        ## 잘랐ㅇ르 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    ## 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    ## 떡의 양이 충ㅇ분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else :
        result = mid ## 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 에 기록
        start = mid + 1

print(f"절단기 최대 값은 = {result}")