#리스트 만들어서 다섯 사람의 이름과 평균을 입력받아 전체 평균을 구하는 코딩
#입력받은 데이터를 (이름, 평균) 출력 후 전체평균 출력

#리스트 생성
nameList = []
numList = []

#입력받기
for i in range (5):
    name, num = input("이름과 평균을 입력해주세요. (입력 예: 홍길동 52) : ").split()
    nameList.append(name)
    numList.append(int(num))

#출력
for t in range(5):
    print(nameList[t], numList[t])
print ("%2.0f" %(sum(numList)//5)) #정수자리까지만 표현
