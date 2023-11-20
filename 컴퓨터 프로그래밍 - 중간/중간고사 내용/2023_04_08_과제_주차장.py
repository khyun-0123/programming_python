from datetime import datetime
import re

#초기 값 세팅
enter_hour = 10000
enter_minute = 10000
enter_time = 0

#현재시간 입력에 대한 세팅
current_time = datetime.now().time()
current_time = current_time.strftime("%H:%M")

#차량번호 입력, 입차시간 입력 및 현재시간 출력, 입차시간 입력 오류 체크, 오류 발생 시 다시 입력받음
print("-------------------------------------------------------------------")
print("상명대학교 무인정산기 입니다. 최대 48시간까지만 주차가능합니다.")
print("주차 시간은 30당 5000원으로 계산되며, 최소 정산 금액은 5000원 입니다.")
print("")
num = str(input("차량번호를 입력해주세요: "))
while enter_hour*100 + enter_minute > 2400 or enter_minute > 60:
    enter_time = str(input("입차시간을 입력해주세요(24시간제): "))
    enter_time_list = re.findall('\d+', enter_time)
    enter_hour = int(enter_time_list[0])
    enter_minute = int(enter_time_list[1])
    if enter_hour*100 + enter_minute > 2400 or enter_minute > 60:
        print ("잘못 입력하셨습니다. 다시 입력해주세요.")
        print("")
print("-------------------------------------------------------------------")
print("현재 시간은", current_time, "입니다.")

#현재시간을 시간, 분 단위로 바꿔서 정리
current_hour = int(current_time[0:2])
current_minute = int(current_time[3:5])

#주차시간(입차시간과 현재시간의 차이)를 계산
park_hour = current_hour - enter_hour
park_minute = current_minute - enter_minute

#주차시간 시간 오류 수정
if park_minute < 0:
    park_hour = park_hour - 1
    park_minute = park_minute + 60
if park_hour < 0:
    park_hour = park_hour + 24
if enter_hour*100+enter_minute > current_hour*100+current_minute:
    park_hour = park_hour + 24

#주차요금 계산
if park_minute % 30 == 0:
    park_fee = (park_hour * 60 + park_minute) // 30 * 5000
else:
    park_fee = (park_hour * 60 + park_minute) // 30 * 5000 + 5000

#주차시간을 출력
print(num, "차량의 주차시간은", park_hour, "시간", park_minute, "분 입니다.")
print("-------------------------------------------------------------------")
print("총 주차요금은", park_fee, "원 입니다.")
print("이용해주셔서 감사합니다.")