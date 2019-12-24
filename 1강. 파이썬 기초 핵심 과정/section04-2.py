# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str('ace')
# 문자열 길이 구하기
print(len(str1), len(str2), len(str3), len(str4)) # 공백도 길이로 포함

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \t Tab \t"
print(escape_str2)

# Raw String 있는 그대로 표시
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
""" 
문자열

멀티라인 테스트 

"""
print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "NiceMan"

print(str_o1 * 100)
print(str_o2+str_o3)
print(str_o1 * 3) #문자열을 반복으로 인식
print('a' in str_o4) #문자열에 해당문자열이 있느냐 
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77) + 'a') #문자열을 취급하기 때문에 컴파일이 된다 
print(str(10.4)) #문자열이다 

# 문자열 함수

a = 'niceman'
b = 'orange'

print(a.islower()) #문자열이 전부 소문자로 되어있니
print(a.endswith('e')) #문자열이 e로 끝나니 
print(a.capitalize()) #문자열 첫번째를 대문자로 바꾼다
print(a.replace('nice', 'good')) # 특정부분을 찾아서 대체 
print(list(reversed(b))) #문자열 역순 

#주석은 블록을 치고 ctrl + ?

print(a[0:3])
print(a[0:4])
print(a[0:7])
print(a[0:len(a)]) #문자열을 직접 count하지않아도 문자열 끝까지 출력할 수 있다
print(a[:4])
print(a[:]) #문자열 전체가 나온다 
print(b[0:4:2]) #처음:끝:점핑할 갯수

print(b[1:-2])
print(b[::-1]) #처음:끝:거꾸로

