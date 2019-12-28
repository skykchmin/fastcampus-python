# Section 06-1
# 파이썬 함수식 및 람다(lamda)
# 함수를 사용하는 이유: 반복적이고 중복적인 프로그래밍을 피할 수 있어서
# 하나의 기능을 하나의 함수로

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parmeter)
# 함수 선언 위치 중요

# return 없는 것
def hello(world):
    print("Hello", world)

hello("Python!")
hello(7777)

# return 있는것
# def hello_return(world):
#     val = "Hello" + str(world)
#     return val

# str = hello_return("python!!!!!")
# print(str)

# 다중 리턴(파이썬에서 허용)
def fun_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

 # 다중 리턴을 할 때 리턴할 것을 생각한다

val1, val2, val3 = fun_mul(100)
print(val1, val2, val3)
print(type(val1))

# 예제4 리스트로 반환 받을 때
def fun_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] 

# 예제5 튜플로 반환 받고 싶을 때 
def fun_mul3(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3)

# *argsm *kwargs 를 사용하는 이유: 매개변수가 몇 개 넘어오는지 모를 때, 매개변수에 따라 동작이 어떻게 동작하는지 다를 때 

def args_func(*args):
    print(type(args))

    for t in args:
        print(t)
    print(args)

# 이뮬레이터 : 인덱스를 붙여주는 게 있음
def args_func2(*args):
   for i,v in enumerate(args):
       print(i, v) # 인덱스를 만들어준다 

args_func('kim') #튜플 형태로 1개를 넘어감
args_func('kim', 'park', 'lee')
args_func2('kim') #튜플 형태로 1개를 넘어감
args_func2('kim', 'park', 'lee')

# kwargs 키워드의 줄임말
# 별표가 하나일 때는 튜플로받는데, 별표가 2개면 딕셔너리로 받는다
def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2 = 'Park', name='Lee')

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs): #arg1, arg2는 필수로 입력 받아야하는 거고 *args는 튜플 형태, **kwargs는 딕셔너리로 입력받는다 (args, kwargs는 가변 )
    print(arg1, arg2, args, kwargs)

example_mul(10, 20) 
example_mul(10, 20, 'park', 'kim', age1= 24, age2 = 35) 

# 중첩 함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)

# 예제 6 
# 힌트란 매개변수 형태가 어떤 게 들어가야하는지 알려주는 것
# 함수의 입력 값과 출력 값을 알 수 있다

def fun_mul4(x : int) -> list: #예를 들면 매개 변수 x에는 int여야해 반환이 되는 것은 리스트여야해  
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(fun_mul4(5)) 

# 람다식 예제
# 람다식 : 메모리 영역, 가독성 향상, 코드 간결 
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10 

var_func = mul_10
print(var_func(10))

lambda_mul_10 = lambda x: x * 10 #x는 input, 출력은 x * 10

print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
    print( x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000))