# 해석방법
# pkg 폴더 안에 피보나치 파이썬 파일안에 대문자 피보나치 클래스 안에 있다 
class Fibonacci:
    def __init__(self, title = "fibonacci"):
        self.title = title

    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end='')
            a, b = b, a+b
        print()

    def fib2(n):
        result = [] #리스트
        a, b = 0, 1
        while a < n:
           result.append(a)
           a, b = b, a+b
           return result
          