food_sum = 0
jja = 0
jjam = 0
guk = 0
hanuguk = 0
orderedList = []

def select1():
    global food_sum, jja, jjam, guk, hanuguk
    print (" --<중 식>------ \n |1. 짜장면 7000| \n |2. 짬  뽕 8000| \n |3. 취  소     |") 
    fd_select = int(input("원하는 메뉴을 입력해 주세요. : "))
    if fd_select == 1:
        food_sum += 7000
        jja += 1
        print("짜장면 하나를 장바구니에 담았습니다. \n ----------------")            
    if fd_select == 2:
        food_sum += 8000
        jjam += 1
        print("짬뽕 하나를 장바구니에 담았습니다. \n ----------------")            
    if fd_select == 3:
        print("취소되었습니다. \n ----------------")

def select2():
    global food_sum, jja, jjam, guk, hanuguk
    print(" --<한 식>------ \n |1. 국  밥 7000| \n |2. 한우국밥 8000| \n |3. 취  소     |")
    fd_select = int(input("원하는 메뉴을 입력해 주세요. : "))
    if fd_select == 1:
        food_sum += 7000
        guk += 1
        print("국밥 하나를 장바구니에 담았습니다. \n ----------------")            
    if fd_select == 2:
        food_sum += 8000
        hanuguk += 1
        print("한우국밥 하나를 장바구니에 담았습니다. \n ----------------")
    if fd_select == 3:
        print("취소되었습니다. \n ----------------")

def select3():
    global food_sum, jja, jjam, guk, hanuguk
    if jja != 0:
        orderedList.append("짜장면 " + str(jja) + "개")
    if jjam != 0:
        orderedList.append("짬뽕 " + str(jjam) + "개")
    if guk != 0:
        orderedList.append("국밥 " + str(guk) + "개")
    if hanuguk != 0:
        orderedList.append("한우국밥 " + str(hanuguk) + "개")
    print(orderedList, "를 주문하셨습니다. 총 가격은", food_sum, "원 입니다.")

while True:
    print("어떤 가게의 메뉴를 장바구니에 담으시겠어요? \n --<가게>-- \n |1. 중 식| \n |2. 한 식| \n |3. 완 료|")
    st_select = int(input("원하는 가게를 골라 주세요. : "))
    if st_select == 1:
        select1()
    if st_select == 2:
        select2()
    if st_select == 3:
        select3()
        break