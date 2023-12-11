# 리스트(List) 비교
list_example = [1, 2, 3, 4, 5]

# 리스트에 요소 추가
list_example.append(6)

# 리스트에서 요소 제거
list_example.remove(3)

# 리스트 슬라이싱
list_slice = list_example[1:4]

# 출력
print("List:", list_example)
print("List Slice:", list_slice)
print()

# 튜플(Tuple) 비교
tuple_example = (1, 2, 3, 4, 5)

# 튜플 슬라이싱
tuple_slice = tuple_example[1:4]

# 출력
print("Tuple:", tuple_example)
print("Tuple Slice:", tuple_slice)
print()

# 세트(Set) 비교
set_example = {1, 2, 3, 4, 5}

# 세트에 요소 추가
set_example.add(6)

# 세트에서 요소 제거
set_example.remove(3)

# 출력
print("Set:", set_example)
print()

# 딕셔너리(Dictionary) 비교
dict_example = {'a': 1, 'b': 2, 'c': 3}

# 딕셔너리에 새로운 키-값 쌍 추가
dict_example['d'] = 4

# 딕셔너리에서 특정 키 제거
del dict_example['b']

# 출력
print("Dictionary:", dict_example)
