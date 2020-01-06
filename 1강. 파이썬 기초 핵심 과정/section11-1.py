# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기
# csv 읽기
# csv 쓰기
# XSL, XLSX 읽기
# csv: MIME - text/csv 포맷으로 구분된 파일

import csv
# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)

    # 확인
    print(reader)
    print(type(reader)) #csc.reader 클래스
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|') #delimiter : ~로 구분되어있다를 알려줌 
    next(reader)
    
    # 확인
    print(reader)
    print(type(reader)) #csc.reader 클래스
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제 3(dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items(): # 한줄을 콜롬명을 토대로 키와 밸류 형태로 
            print(k, v)
        print('------------')

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13,14,15],[16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f: #newline 옵션은 엔터가 두번쳐지는것을 한번 쳐지는 것으로 바꿀 수 있다
    wt = csv.writer(f) #하나의 리스트는 한줄로 들어감

    for v in w:
        wt.writerow(v)


# 예제5 for문을 쓰지않고 한번에
with open('./resource/sample4.csv', 'w', newline='') as f: #newline 옵션은 엔터가 두번쳐지는것을 한번 쳐지는 것으로 바꿀 수 있다
    wt = csv.writer(f)
    wt.writerows(w) #리스트를 한번에 씀 // for문을 쓰지 않고 

# 예제4,5의 차이점: 예제4는 한줄 한줄 쓰는것은 if로 검증을 하는거고 예제5는 검증이 끝난 데이터를 한번에 넣는것



# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwy, xluitls
# panadas 를 주로 사용 (openpyxl, xlrd) 내부적으로 사용하기 때문에 csv, 텍스트파일을 자유롭게 사용할 수 없다
# 설치 과정
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname ='시트명' 또는 숫자, header = 숫자, skiprow = 숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head()) # 데이터를 5개만 보여준다
print()

# 데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) # 행, 열 확인

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.xlsx', index=False)
