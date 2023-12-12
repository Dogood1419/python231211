# class 이해

class person():
    # 초기화 루틴을 실행
    def __init__(self):
        #인스턴스 멤버 변수
        self.name = "default name"
    def print(self):
        print ('My name is {0}'.format(self.name))

#2 인스턴스 (복사본을 생성
p1= person()
p2= person()
# p1.name = "강감찬"
#3 메서드 호출
# p1.print()
# p2.print()

# 런타임시 변수 추가
person.title = "New Title"
print (p1.title)
print (p2.title)
print (person.title)

