import time

print("[start] ex_euclidean_algo.py")
start_time = time.time() # 측정 시작

'''
유클리드 호제법 : 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘
두 자연수 A, B 에 대해서(A>B) A를 B로 나눈 나머지를 R이라고 할 때, 
A, B의 최대공약수 = B, R의 최대공약수
GCD : 최대공약수
'''
def gcd(a, b):
    if a % b == 0:
        return b
    else :
        return gcd(b, a%b)
print(gcd(192, 162))

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
