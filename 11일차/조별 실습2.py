# csv flie을 읽어서 data frame을 작성한다.
# data frame 내용을 출력한다.

f = open('C:/Users/CPB06GameN/Desktop/새 폴더_2/시군구_대전_의료보장_적용인구_현황_20190718170231txt.txt','r')
lines = f.readlines()
count = 0
a = int(input('숫자형으로 바꿀 열 번호 입력( 없으면 -1라고 입력 ):'))
column_list = lines[0].split(',')
print(column_list)
dt = []
for line in lines[1:]:
    line = line.split(',')
    count += 1
    if a != -1:
        line[a] = int(line[a])
    dt.append(line)
    print(line)
print(dt)
f.close()

lista = []
for i in range(len(line)):
    lista.append([])
for i in range(len(line)):
    for j in range(len(dt)):
        lista[i].append(dt[j][i])
print(lista)

# data frame의 변수 속성을 출력한다.

b = int(input('속성을 알고 싶은 열 번호 입력:'))
print(type(line[b]))

# data frame의 data와 변수의 수를 출력한다.

print(count) # 행의 개수
print(len(line)) # 변수의 수

# data frame의 변수 항목을 리스트로 만든다.

print(lines[0].split(','))

# data frame의 앞부분 일정 부분의 내용을 출력한다.

for line in lines[1:3]:
    line = line.split(',')
    print(line)

# data frame의 뒷부분 일정 부분의 내용을 출력한다.

for line in lines[count-1:]:
    line = line.split(',')
    print(line)

# data frame의 변수 이름을 변경하는 기능을 제공한다.

c = int(input('변경할 변수 이름의 열 번호 입력:'))
d = str(input('바꿀 변수 이름:'))
column_list[c] = d

print(column_list)

# data frame에 파생 변수를 추가하는 기능을 제공한다.

