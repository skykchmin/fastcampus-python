# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중 상속

# 예제1
# 상속 기분
# 슈프클래스(부모) 및 서브클래스(자식) - > 모든 속성, 메소드 사용 가능

# 상속의 필요성
# 코드 재사용, 중복을 최소화 >> 생산성, 유지보수 가능

# ex) 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 공통적인 속성 >> 부모


class Car:
    """Parent class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
    
    def  show(self):
        return 'Car class "Show Method!"'

class BmwCar(Car):
    """Sub class"""
    def __init__(self, car_name, tp, color): #tp, color는 부모한테 넘겨줘야함
        super().__init__(tp, color) #부모의 init 메서드를 호출
        self.car_name = car_name
    
    def show_model(self) -> None: #힌트로 리턴값이 없다
        return "Your car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub class"""
    def __init__(self, car_name, tp, color): #tp, color는 부모한테 넘겨줘야함
        super().__init__(tp, color) #부모의 init 메서드를 호출
        self.car_name = car_name
    
    def show_model(self) -> None: #힌트로 리턴값이 없다
        return "Your car Name : %s" % self.car_name
    def show(self): 
        print(super().show()) # 오버라이딩 했지만 부모 것도 호출하고 싶을 때 
        return 'Car Info: %s %s  %s' %(self.car_name, self.type, self.color)
# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__) # 부모, 자식 namespace

# Method Overriding(오버라이딩)
# 오버라이딩 : 올라타다 // 내 목적에 맞게 부모 클래스의 메서드를 자식클래스에서 바꾸는 것 

model2 = BenzCar("220d", 'suv', "black")
print(model2.show())

# Parent Method Call
# 부모를 다이렉트로 부르는법

model3 = BenzCar("350s", "sedan", "silver")
print(model3.show())

# Inheritacne Info : 상속 관계가 깊을 때 상속 정보를 나타내주는 
print(BmwCar.mro()) # 왼쪽에서 오른쪽으로 상속 관계 bmw는 car클래스를 상속받고 car클래스는 obk클래스로 상속받는다
print(BenzCar.mro())

# 예제2
# 다중 상속
# 너무 복잡한 상속은 코드의 가독성이 떨어진다

class X():
    pass

class Y():
    pass

class Z():
    pass 

class A(X, Y): #클래스 A는 X와 Y를 상속받겠다 
    pass

class B(Y, Z):
    pass 

class M(B, A, Z): #파이썬에서는 다중상속 가능
    pass

print(M.mro())
print(A.mro())