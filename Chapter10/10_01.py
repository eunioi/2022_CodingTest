'''
그래프 알고리즘을 다룸
크루스칼 알고리즘 - 그리디 알고리즘
위상 정렬 알고리즘 - 큐 자료 구조 or 스택 자료구조를 활용
그래프 : 노드-노드 사이에 연결된 간선 의 정보를 가지고 있는 자료구조를 의미함.
'서로 다른 개체(혹은 객체)가 연결되어 있다. -> 그래프 알고리즘을 떠올려야함.

그래프 구현 방법
- 인접행렬 : 2차원 배열을 사용하는 방식
- 인접 리스트 : 리스트를 사용하는 방식

최단 경로를 찾아야하는 문제 출시
- 노드의 개수가 적은 경우 : 플로이드 워셜 알고리즘 사용
- 노드의 개수가 많은 경우 : 우선순위 큐를 이용하는 익스트라 알고리즘을 사용

서로소 집합
- 공통원소가 없는 두 집합
- union-find 자료구조라고 불리기도 함

알고리즘은 다음과 같다.
1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
    Ⅰ. A와 B의 루트 노드 A', B'를 각각 찾는다.
    Ⅱ. A'를 B'의 부모 노드로 설정한다. (B' 가 A'를 가리키도록 한다.)
2. 모든 union(합집합) 연산을 처리할 때까지 Ⅰ. 의 과정을 반복한다.

'''

'''
기본적인 서로소 집합 알고리즘 소스코드
'''
## 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    ## 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

## 두원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

print("노드의 개수와 간선(union 연산)의 개수 입력받기")
v, e = map(int, input().split())
parent = [0] * (v+1) ## 부모 테이블 초기화

## 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

## union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
## 각 원소가 속한 집합 출력
print("각 원소가 속한 집합 : ", end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')

print()

## 부모 테이블 내용 출력
print("부모 테이블 : ", end ='')
for i in range(1, v+1):
    print(parent[i], end=' ')
    