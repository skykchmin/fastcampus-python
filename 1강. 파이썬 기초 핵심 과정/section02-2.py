# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
# uft-8을 사용
print(sys.stdin.encoding) #입력,출력이 utf-8로 인코딩 되어있다
print(sys.stdout.encoding)

# 출력문
print('My name is Goodboy!')

# 변수 선언
myName = 'Goodboy'

# 조건문
if myName == 'Goodboy':
    print('OK')

# 반복문
for i in range(1, 10):
    for j in range(1,10):
        print('%d * %d = ' %(i, j), i*j)

# 변수 선언(한글)

이름 = "좋은 사람"
print(이름)

# 함수 선언

def 인사():
    print("안녕하세요. 반갑습니다.")

인사()

# 함수 선언(영문)
def greeting():
    print('Hello!')

greeting()

# 클래스 
class Cookie:
    pass

# 객체 (인스턴스)

cookie = Cookie()

print(id(cookie))
print(dir(cookie))