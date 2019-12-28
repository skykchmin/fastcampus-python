# Section 07-1
# 파이썬 클래스 상세 이해 
# self, 클래스, 인스턴스 변수 

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 각각의 객체르를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성후 사용한다 

# 선언

# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
class Info: #클래스는 첫글자 대문자, 단어와 단어가 연결될때 대문자
    # 속성, 메소드로 클래스는 구성
    pass #함수가 없을 때나 클래스가 없을 때 에러를 없애기 위해서 

# 예제2
class UserInfo:
    def __init__(self, name): #class를 초기화
        self.name = name 
    def user_info_p(self):
        print("초기화:", self.name)

user1 = UserInfo("Kim")
user1.user_info_p()

user2 = UserInfo("Park")
user2.user_info_p()

# 예제 3
# self의 이해
class SelfTest:
    def fuction1(): #클래스 메서드
        print("fuction1 called")
    def fuction2(self): #인스턴스 메서드 // self 인스턴스를 생성해야 fuction호출 가능 
        print(id(self))
        print("fuction2 called")

self_test = SelfTest()
#self_test.fuction1 // 에러가 나는 이유: self가 없기 때문에 누구의 fuction1인줄 모른다
SelfTest.fuction1() # 클래스에서 호출하면 출력가능 
self_test.fuction2() 

print(id(self_test))
SelfTest.fuction2(self_test)

# 예제 4
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수 : 클래스 변수는 self 가 없다// 여러 인스턴스에서 공유!!!!!!! 
    # 하나의 변수로 인해서 공유 
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1 # self가 없기 때문에 클래스에서 직접 접근
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('kim')
user2 = WareHouse('Park')
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) #클래스 네임스페이스 ,클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) #자기 네임스페이스에 없으면 클래스 네임스페이스로 가서 찾고 없으면 에러 
print(user2.stock_num)
print(user3.stock_num)

del user1

print(user2.stock_num)
print(user3.stock_num)
