# Sectio04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pack', 'Banana','Orange'] # 자료형이 달라도 가능
e = [10, 100, ['Pack', 'Banana','Orange']] # 리스트 안에 리스트도 가능 

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1]) #인덱스 안에 인덱스 
print(e[-1][-2])

# 슬라이싱 
print(d[0:3])
print([e[2][1:3]])

# 연산
print(c + d)
print(c * 3)
print(str(c[0])+ 'hi') #인테져를 문자열로 바꾼다음에 

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c'] # 리스트안에 리스트가 통째로 들어갔다 하나의 인덱스를 잡고 넣으면 리스트가 다 들어간다
print(c)

del c[1] # 요소 삭제
print(c)

del c[-1]
print(c)

# 리스트 함수 
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 리스트 끝부분에 추가
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7) #2번 인덱스에 요소 7을 추가할거야
print(y)
y.remove(2) # del일 때는 인덱스를 찾아가서 지웠지만, remove일 때는 요소 2를 찾아가서 지웠다 
print(y)
y.pop()
print(y) # 맨 마지막 요소를 꺼내고 없앤다 LIFO(스택)
ex = [88, 77]
y.extend(ex)
print(y)

# 삭제 : del, remove, pop

# 튜플(순서o, 중복o, 수정x, 삭제x)

a = () # 튜플은 소괄호
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d) # 튜플은 리스트와 마찬가지로 합치기 가능
print(c * 3)
print()
print()
#del c[2] // 지원하지 않는다

# 튜플 함수

z = (5, 2, 1, 3, 4)

print(z)
print(3 in z)
print(z.index(4)) # 4이있는 인덱스를 반환한다
print(z.count(1))

