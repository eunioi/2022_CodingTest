'''
파이썬 이진 탐색 ㅂ라이브러리
bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽일할 가장 왼쪽 인덱스를 반환
bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
'''
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 5, 8]
x = 9

print(bisect_left(a, x))
print(bisect_right(a, x))

'''
값이 특정 범위에 속하는 데이터 개수 구하기
'''
print("값이 특정 범위에 속하는 데이터 개수 구하기")
## 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

## 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]


print(f"값이 3인 데이터 개수 출력 = {count_by_range(a, 3, 3)}")
print(f"값이 [-1, 3] 범위에 있는 데이터 개수 출력 = {count_by_range(a, -1, 3)}")

## 이걸 선언으로 안하고 입력으로 받고싶다면
print("데이터의 개수 N, 찾고자 하는 값 x 받기")
n, x = map(int, input().split())
print("전체 데이터 입력 받기") 
array = list(map(int, input().split()))

## 값이 [x, x] 범위에 있는 데이터의 개수 계싼
count = count_by_range(array, x, x)

## 값이 x 인 원소가 존재하지 않는다면
if count == 0:
    print(f"입력한 '{x}' 인 원소가 존재하지 않습니다.")
## 값이 x인 원소가 존재한다면
else:
    print(f"입력한 '{x}' 인 원소가 존재한데 = ", count)

'''
트리 자료 구조 
- 노드와 노드의 연결로 표현
- 노드 : 정보의 단위로서 어떠한 정보를 가지고 있는 개체
트리 자료구조 특징
- 부모 노드와 자식 노드의 관계로 표현됨
- 루트 노드 : 트리의 최상단 노드
- 단말 노드 : 트리의 최하단 노드
- 서브 트리 : 트리에서 일부를 떼어내도 트리구조이며, 192쪽의 그림을 잘 기억하자.
- 트리는 계층적이고 정렬된 데이터를 다루기에 적합함 
'''

'''
이진 탐색 트리
- 트리 자료구조중 가장 간단한 형태
- 이진 탐색이 동작 할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조 

모든 트리가 다 이진 탐색트리는 아니며, 다음과 같은 특징을 가짐
- 부모 노드보다 왼쪽 자식 노드가 작다.
- 부모 노드보다 오른쪽 자식 노드가 크다. 
=> 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드가 성립해야한다.  
'''



