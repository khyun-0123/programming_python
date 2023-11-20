print ("10시가 되었습니다. 체크를 시작합니다.")
age = str(input("주민번호 앞자리를 입력해주세요: "))
if (int(age[0]) == 0):
    if (4 < int(age[1])):
        print("미성년자 분들은 퇴장해주세요")
else:
    print ("확인 감사합니다.")
