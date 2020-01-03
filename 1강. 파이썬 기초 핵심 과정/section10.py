# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('Test)

# if True
#     pass
# x => y

# NameError : 참조변수 없음
a = 10
b = 15
# print(c)

# ZeroDivisionError : 0으로 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3]) # 예외 발생

# KeyError
dic = {'name' : 'Kim', "Age": 33, 'City' : 'Seoul'}
# print(dic['hobby']) #다이렉트로 접근하지말것
print(dic.get('hobby')) # get 메서드를 이용하면 없을 경우 none을 리턴

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month()) # 어트리뷰트가 없다

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]

# x.remove(10) #10이 포함되어있지 않다
# x.index(10) #10의 참조값이 없다

# FileNotFoundError
# f = open('test.txt', 'r') #현재 경로에 없다

# TypeError

x = [1,2]
y = (1,2)
z = 'test'

# print(x + y) # 튜플과 리스트는 결합할 수 없다
# print(x + z) # 튜플과 리터럴은 결합할 수 없다

# -------------------------------
# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAPP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError: #값이 없을경우
    print('Not found it! - Occured ValueError!')
else:
    print('OK! else!')



# 예제2
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except: #모든 에러가 날지 모를경우 except 하면 다 처리 
    print('Not found it! - Occured ValueError!')
else:
    print('OK! else!')




# 예제3
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except: #모든 에러가 날지 모를경우 except 하면 다 처리 
    print('Not found it! - Occured ValueError!')
else:
    print('OK! else!')
finally:
    print('finally ok!') #예외가 발생하든 발생하지 않든 처리해야한다 


# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('OK Finally!!!')


# 예제5
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l: #에러를 순서대로 잡는다 
    print(l)
except IndexError: 
    print('Not found it! - Occured IndexError!')
except Exception: # Exception은 모든 에러를 잡기 때문에 순서가 중요 
    print('Not found it! - Occured ValueError!')
else:
    print('OK! else!')
finally:
    print('finally ok!') #예외가 발생하든 발생하지 않든 처리해야한다 

# 예제6
# 예외 발생 : raise 
# raise 키워드로 내가 직접 에러를 발생 

try:
    a = '333'
    if a =='Kim':
        print('Ok 허가!')
    else: 
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else: 
    print('OK!')