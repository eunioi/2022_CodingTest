import time

print("[start] ex_stack.py")
start_time = time.time() # 측정 시작

''' 
스택 : FILO 먼저 들어온 데이터가 나중에 나감 (선입후출)
'''
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) ## 최상단 원소부터 출력
print(f"stack = {stack}")

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력