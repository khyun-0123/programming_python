#로또 프로그램 (1~45까지 중 6개 선택)
import random
import time

#수동/자동 선택
select = input("로또 프로그램을 시작합니다. 수동/자동을 선택해주세요: ")

#수동 선택한 경우, 직접 숫자 6개 형식 맞춰 입력 (중복하여 입력할 경우, 범위에 넘는 숫자 입력할 경우 다시 입력)
if select == "수동":
    while True:
        pick1, pick2, pick3, pick4, pick5, pick6 = map(int, input("1~45 사이의 숫자 6개를 입력해주세요.(입력예시: 1 2 3 4 5 6): ").split())
        picklist = [pick1, pick2, pick3, pick4, pick5, pick6]
        if (((picklist.count(pick1) + picklist.count(pick2) + picklist.count(pick3)
            +picklist.count(pick4) + picklist.count(pick5)+ picklist.count(pick6)) == 6)
            and (pick1 <= 45 and pick2 <= 45 and pick3 <= 45 and pick4 <= 45 and pick5 <= 45 and pick6 <= 45)):
            break

#자동 선택한 경우, 랜덤으로 숫자 6개 생성 (count 활용해 중복하는 것 없을 때까지 반복)
elif select == "자동":
    while True:
        pick1 = random.randint(1, 45)
        pick2 = random.randint(1, 45)
        pick3 = random.randint(1, 45)
        pick4 = random.randint(1, 45)
        pick5 = random.randint(1, 45)
        pick6 = random.randint(1, 45)
        picklist = [pick1, pick2, pick3, pick4, pick5, pick6]
        if (picklist.count(pick1) + picklist.count(pick2) + picklist.count(pick3)
             +picklist.count(pick4) + picklist.count(pick5)+ picklist.count(pick6)) == 6:
            break

#로또 번호 체크
print("당신의 로또 번호는", pick1, pick2, pick3, pick4, pick5, pick6, "입니다.")
time.sleep(1)

#당첨번호 생성 (count 활용해 중복하는 것 없을 때까지 반복)
print("추첨을 시작합니다.")
while True:
    lotto1 = random.randint(1, 45)
    lotto2 = random.randint(1, 45)
    lotto3 = random.randint(1, 45)
    lotto4 = random.randint(1, 45)
    lotto5 = random.randint(1, 45)
    lotto6 = random.randint(1, 45)
    lotto7 = random.randint(1, 45)
    lottolist = [lotto1, lotto2, lotto3, lotto4, lotto5, lotto6]
    if (lottolist.count(lotto1) + lottolist.count(lotto2) + lottolist.count(lotto3)
        + lottolist.count(lotto4) + lottolist.count(lotto5) + lottolist.count(lotto6)) == 6:
        break

#당첨번호 출력
print("당첨번호는\n두구두구두구")
time.sleep(1)
print(lotto1, lotto2, lotto3, lotto4, lotto5, lotto6, "보너스 번호는", lotto7, "입니다.")


#당첨여부 확인, 등수 출력
dang_chum = lottolist.count(pick1) + lottolist.count(pick2) + lottolist.count(pick3) + lottolist.count(pick4) + lottolist.count(pick5) + lottolist.count(pick6)
bonus_num = picklist.count(lotto7)

if dang_chum == 6:
    print("1등입니다.")
elif dang_chum == 5 and bonus_num == 1:
    print("2등입니다.")
elif dang_chum == 5:
    print("3등입니다.")
elif dang_chum == 4:
    print("4등입니다.")
elif dang_chum == 3:
    print("5등입니다.")
else:
    print("꽝입니다. 다음 기회에 도전하세요.")