'''
여기서는 계수 정렬로 해결할거야
1. 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든다.
2. 리스트의 인덱스에 직접 접근하여 특정한 번호의 부품이 매장에 존재하는지 확인한다.
'''

print("N(가게의 부품 개수) 입력 ↓")
n = int(input())
array = [0] * 1000001

print("가게에 있는 전체 부품 번호를 입력받아서 기록")
for i in input().split():
    array[int(i)] = 1

print("M(손님이 확인 요청한 부품 개수)을 입력받기")
m = int(input())
print(" 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력")
x = list(map(int, input().split()))

## 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x :
    ## 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ' )