# 데이터 타입

v_str1 = "NiceMan"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}

v_list = [3, 5, 7] #배열
v_tuple = 3, 5, 7
v_set = {7, 8 ,9}

print(type(v_tuple))
print(type(v_set))
print(type(v_float)) #자료형이 뭔지 알 수 있는 명령어

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999
big_int1 = 777777777777777

print(i1*i2)

a = 5. 
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환(캐스팅)
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3)) # 실수 부분과 허수부분을 나타낸다
print(int(True)) # true = 1, false = 0
print(int('3'))
print(complex(False))

y = 100
y += 100
print(y)

# 수치 연산 함수

print(abs(-7)) #부호 반대로
n, m = divmod(100,8) # 100을 8로 나눠소 몫은 n, 나머지는 m

import math #수학관련 임포트

print(math.ceil(5.1)) # 5.1보다 크면서 가장 작은 정수는
print(math.floor(3.874)) # 3.874보다 작으면서 가장 큰 정수 