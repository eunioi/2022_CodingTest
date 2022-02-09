'''
실전 문제 부품 찾기
다량의 데이터 검색은 이진 탐색 알고리즘을 이용하는 것이 효과적이다.
1. 매장 내 N개의 부품을 번호를 기준으로 정렬 할 것
2. M개의 찾고자 하는 부품이 각각 매장에 존재하는지 검사
이때 정렬 되어있는 것이 포인트

여기서는 이진탐색으로 해결할 거야
'''

## 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        ## 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        ## 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

print("N(가게의 부품 개수) 입력 ↓")
n = int(input())
print("가게에 있는 전체 부품 번호를 공백으로 구분하여 입력 ↓")
array = list(map(int, input().split()))
array.sort() ## 이진 탐색을 수행하기 위해 사전에 정렬 수행
print("M(손님이 확인 요청한 부품 개수) 입력 ↓")
m = int(input())
print("손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력")
x = list(map(int, input().split()))

##  손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x :
    ## 해당 부품이 존재하는 지확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print("yes", end = ' ')
    else:
        print('no', end = ' ')

