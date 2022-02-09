array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(f"sorted 사용 결과 = {sorted(array)}")

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
print(f"sort 사용 결과 = {array}")

## sorted() OR sort()를 사용할 때 key 매개변수를 입력으로 받을 수 있다.
print("key를 활용한 소스코드")
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting)
print(f"최종 결과 : {result}")

 
