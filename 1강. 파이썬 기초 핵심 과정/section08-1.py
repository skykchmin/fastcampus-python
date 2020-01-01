# Section08-1
# 모듈: 파일 하나하나
# 패키지: 모듈들을 디렉터리 구조적으로 관리하는것 

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 상대 디렉토리 
# 파일 이름이 중요 : 파일 이름을 통해서 모듈이 어떤 역할을 하는지 알아야되기 때문에 네이밍 중요

# 사용1(클래스)
from pkg.fibonacci import Fibonacci 

Fibonacci.fib(300)

print("ex2: ", Fibonacci.fib2(400))
print("ex2: ", Fibonacci().title)

# 사용2(클래스) // 권장하지는 않는다 메모리를 많이 씀
from pkg.fibonacci import * 

print("ex2: ", Fibonacci.fib2(500))
print("ex2: ", Fibonacci().title)

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb 

fb.fib(1000)

print("ex3: ", fb.fib2(400))
print("ex3: ", fb().title)

# 사용4(함수)
import pkg.calculations as c # 함수 단위기 때문에 

print("ex4: ", c.add(10,100))
print("ex4: ", c.mul(10,100))

# 사용5(함수)
from pkg.calculations import div as d # 모든 함수를 사용하지 않기 때문에 필요한 함수만 가져옴
print("ex5: ", int(d(100,10)))

# 사용6
import pkg.prints as p
import builtins # 파이썬에서 기본으로 제공하는 함수 
p.prt1()
p.prt2()
print(dir(builtins))