# 람다함수
# g = lambda x,y : x * y
# print (g(3,4))

# print ((lambda x: x * x)(3))

# print (globals())

# print("---필터링---")

# 블럭으로 주석 처리하기 : ctrl + /

# lst = [10,20,30]
# iteml = filter(lambda lst)
# print (iteml)

# 분기구문


# 반복구문

# value = 5
# while value > 0 :
#     print (value)
#     value -= 1

# fruits = {'apple':10, 'kiwi':20}
# for item in fruits.items():
#     print(item)

# print("---list 내장----")
# lst = list (range(1,11))
# print ([i**2 for i in lst if i >5])

# tp = ('apple', 'kiwi', 'pineapple')
# print ([len(i) for i in tp])

# 구구단 출력
# for i in range(2,10):
#     print ('{0}단 출력'.format(i))
#     for j in range(1,10):
#         print("{0}*{1} = {2}".format(i,j,i*j))

# f-string 문법을 사용
for i in range(2,10):
    print (f'{i}단 출력')
    for j in range(1,10):
        print(f"{i}*{j} = {i*j}")

