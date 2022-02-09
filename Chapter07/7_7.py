'''
집합 자료형 이용하여 해결
set() 함수 : 집합 자료형을 초기화 할 때 사용한다.
이 소스코드가 간결한 측면에서는 가장 우수하다고 할 수 있다.
'''

print("N(*가게의 부품 개수)을 입력받기 ↓")
n = int(input())
print("가게에 있는 전체 부품 번호를 입력받아 집합(set) 자료형에 기록")
array = set(map(int, input().split()))

print("M(손님이 확인 요청한 부품 개수)을 입력받기")
m = int(input())
print("손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력받기 ↓")
x = list(map(int, input().split()))

## 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    ## 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end = ' ') 
    else:
        print('no', end = ' ')
