import time

print("[start] ex_queue.py")
start_time = time.time() # 측정 시작

''' 
큐 : FIFO, 선입선출
'''
from collections import deque
## 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) ## 먼저 들어온 순서대로 출력
queue.reverse() ## 역순으로 바꾸기
print(queue) ## 나중에 들어온 원소부터 출력

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력