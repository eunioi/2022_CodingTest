print("[start] 퀵 정렬 소스코드 ")

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: ## 원소가 1개인 경우 종료
        return

    ## 이제 원소가 1개가 아닌 경우
    pivot = start ## 피벗은 첫 번째 요소
    left = start +1 ## 첫번째 원소를 제외하고, 가장 왼쪽을 left 로 설정
    right = end ## 가장 오른쪽을 right 로 설정
    while left <= right: ## 엇갈릴 때까지 반복한다는 의미
        ## 피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        ## 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right : ## 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: ## 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    ## 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
print(f"최종결과 = {array}")

 
