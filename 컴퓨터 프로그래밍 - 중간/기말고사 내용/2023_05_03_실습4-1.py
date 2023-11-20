#5사람의 이름, 전화번호를 리스트에 저장한 후 검색을 톻해 이름을 입력하면 전화번호를 출력

#리스트 생성
nameList = []
numList = []

#입력받기
for i in range (5):
    name, num = input("이름과 전화번호를 입력해주세요. (입력 예: 홍길동 01012341234) : ").split()
    nameList.append(name)
    numList.append(int(num))

#검색하면 전화번호 알려주기
while True:
    findname = input("찾을 이름을 입력해주세요: ")
    location = nameList.index(findname)
    print(numList[location])