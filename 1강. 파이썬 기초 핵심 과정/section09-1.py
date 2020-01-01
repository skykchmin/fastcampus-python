# Section90
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기본 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대 경로
# . : 절대 경로

# 파일 읽기
# 예제1

f = open('./resource/review.txt', 'r') # 파일을 열 때는 파일의 경로를 입력후 모드 선택
content = f.read()
print(content)
print(dir(f)) # 메소드 인스턴스를 확인할 수 있다.
# 반드시 close 리소스 반환 // 한번 사용한 리소스는 닫아야한다
f.close()

print("-----------------")
print("-----------------")

with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c)) #리스트로도 바꿀수 있음
# with close를 해주지 않아도 read문이 끝나면 close를 해줌


print("-----------------")
print("-----------------")

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f: 
        print(c.strip()) # 라인 단위로 읽어온다 

print("-----------------")
print("-----------------")

# 에제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 커서가 끝으로 읽어오기 때문에 내용 없음
    print(">", content) 

print("-----------------")
print("-----------------")   

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline() # 커서가 1줄로 위치

    while line: 
        print(line, end=' ##### ') # 한 줄씩 읽어옴 
        line = f.readline()

print("-----------------")
print("-----------------")

# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents) #모든 문장을 엔터를 기준으로 리스트 형태로 가지고 있음
    for c in contents:
        print(c, end=' ******')

print("-----------------")
print("-----------------")

# 예제7
score = []
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line)) #문자열로 읽어오기 때문에 형변환
    print(score)

print('Average : {:6.3}'.format(sum(score)/ len(score))) #6자리도 3째짜리까지 나와라

# 파일 쓰기

# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')

# 예제2
with open('./resource/text1.txt', 'a') as f: # 기존 파일에 추가
    f.write('Goodman!\n')

# 예제3
from random import randint

with open('./resource/text2.txt', 'w') as f: 
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4

with open('./resource/text3.txt', 'w') as f: 
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

# 예제5
with open('./resource/text3.txt', 'w') as f: 
    print('Test Conteststs1!', file = f)
    print('Test Conteststs2!', file = f)