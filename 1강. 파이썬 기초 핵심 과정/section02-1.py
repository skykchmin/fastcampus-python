# Section02-1
# 파이썬 기초코딩
# Print 구문의 이해

# 기본출력
print('Hello Python!') 
print("Hello python!") 
print("""Hello python!""")
print('''Hello python!''')

print() #줄바꿈

# Separator 옵션 사용

print('T', 'E', 'S', 'T', sep='') #작은따옴표 사이값에 나오는 문자열을 이어주고 있다
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep = '@') #,로 연결(조인)을 하고싶을때 sep = 사용한다

# end 옵션 사용
print('Welcome To', end='')
print(' the black parade', end='') #끝부분을 end부분으로 연결시켜주는 것 
print(' piano notes') 

print()

# format 사용 [], {}, () 괄호에 값을 넣을 때 
print('{} and {}'.format('You', 'Me')) #포맷형식으로 문자열을 넣을수 있다
print("{0} and {1} and {0}".format('You','Me')) #문자열 반복시킬수 있음
print("{a} are {b}".format(a='You', b ="Me"))

print("%s's favorite number is %d" % ('Min', 7)) #%s: 문자, %d: 정수, %f: 실수

print("Test1: %5d, Price: %4.2f" % (776, 6534.123)) 
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123)) #0은 5자리 정수이다 
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))


print("'you'")
print('\'you\'') #escape: \ 
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('test')

