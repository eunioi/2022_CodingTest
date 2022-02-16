'''
다이나믹 프로그래밍을 적용했을 때 시간복잡도 = O(N)

호출 되는 함수 확인
'''
print("호출 되는 함수 확인")
d = [0] * 100

def pibo(x):
    print('\nf(' + str(x) + ')', end = ' ')
    if x == 1 or x == 2:
        return 1
    ## 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    ## 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]


cnt = 99
print(f"x = {cnt}, {cnt} 번째 피보나치 수열 값은 {pibo(cnt)}")
