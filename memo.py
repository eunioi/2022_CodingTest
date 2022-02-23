'''
Chapter 09 : 최단 경로 문제
            - 가장 짧은 경로를 찾는 알고리즘
            - 노드 : 각 지점
            - 간선 : 지점 간 연결된 도로
                    간선에 방향을 표현 할 수 도 있데

다익스트라 최단 경로 알고리즘
- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
- 현실 세계의 도로(간선) 알고리즘으로 활용할 수 있음
- 매 상황에서 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복함 ( 그리디 알고리즘 )

알고리즘의 동작 과정
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화(내 노드는 0, 모든 노드까지 가는 비용은 무한대) 한다. // 무한대를 쓸 때는 int(1e9) 를 사용함.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다. -> 이것으로 그리드 알고리즘으로 분류된다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 3-4 번을 반복한다.

다익스트라 알고리즘 구현방법
1. 구현하기 쉽지만 느리게 동작하는 코드
2. 구현하기 어렵지만 빠르게 동작하는 코드

다익스트라 최단 경로 알고리즘에서는 '방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택' 하는 과정을 반복 함.
+ 한 단계당 하나의 노드에 대한 최단 거리를 확실히 ㅊ ㅏㅈ는 것으로 이해할 수 있다.

간단한 다익스트라 알고리즘의 시간 복잡도 : O(V²)
v = 노드의 개수


'''