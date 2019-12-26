# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제 o

# key, value (Json) -> 몽고DB
# 선언 // 키를 가지고 value값을 얻는다

a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello Coding'} #딕셔너리는 중괄호 사용 
c = {'arr': [1, 2, 3, 4, 5]} 

print(type(a))

#출력
print(a['name'])
print(a.get('name')) # 조회할때 안전하게 접급하기 위해서는 get메서드를 사용한다 
print(a.get('address'))
print(c['arr'][1:3]) #키를 가진 value 리스트를 가져와서 출력

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank'] = (1,2,3,)
print(a)

# key, values, items // item key + value를 합친 상태
print(a.keys()) #키만 리스트 형태로 가져온다
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values()) # value만 리스트 형태로 가져온다 
print(list(a.values()))

print(a.items()) # key , value형태로 가져온다
print(list(a.items()))
print(2 in b)
print('name' in a)

# 집합(Sets) (순서x, 중복x)

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c) # 6이 두번 안나오는데 중복을 허용하지 않기 때문에

t = tuple(b)
print(t) # ()로 바뀜
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))


print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7) #중복이 있기 때문에 추가 안됨

print(s3)

s3.remove(15)
print(s3)

print(type(s3))