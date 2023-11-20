#전화번호 딕셔너리
numLib = {
    '인천_김재현': {'전화번호': '010-1234-5678'},
    '서울_홍길동': {'전화번호': '010-2345-6789'},
    '부산_김진희': {'전화번호': '010-3456-7890'},
    '보령_신기문': {'전화번호': '010-4567-8901'},
    '광주_김준현': {'전화번호': '010-5678-9012'},
    '익산_최준수': {'전화번호': '010-6789-0123'},
    '수원_이승찬': {'전화번호': '010-7890-1234'},
    '청주_반준호': {'전화번호': '010-8901-2345'},
    '서울_차준영': {'전화번호': '010-9012-3456'},
    '창원_홍윤성': {'전화번호': '010-0123-4567'},
    '해남_홍길동': {'전화번호': '010-9876-5432'}
}

while True:
    print("<메뉴> \n1 : 전화번호부 검색 \n2 : 전화번호부 추가 \n3 : 전화번호부 수정 \n4 : 전화번호부 삭제")
    select = int(input("원하는 메뉴를 입력해 주세요. : "))

    if select == 1:
        findname = input("전화번호 검색 기능입니다. \n찾으실 이름을 입력해주세요(ex. 인천_김재현). : ")
        if findname in numLib:
            print("이름:", findname)
            print("전화번호:", numLib[findname]['전화번호'])
        else:
            print("해당 이름을 찾을 수 없습니다.")
            
    elif select == 2:
        print("전화번호 추가 기능입니다. \n추가할 이름을 입력해주세요(ex.인천_김재현).")
        name = input("이름: ")
        if name in numLib:
            print("이미 존재하는 이름입니다. 다른 이름을 입력해주세요.")
            continue
        phone_number = input("전화번호(ex.010-1234-5678): ")
        numLib[name] = {'전화번호': phone_number}
        print("전화번호가 추가되었습니다.")

    elif select == 3:
        print("전화번호 수정 기능입니다. \n수정할 이름을 입력해주세요(ex.인천_김재현).")
        name = input("이름: ")
        if name not in numLib:
            print("해당 이름을 찾을 수 없습니다.")
            continue
        phone_number = input("수정된 전화번호(ex.010-1234-5678): ")
        numLib[name] = {'전화번호': phone_number}
        print("전화번호가 수정되었습니다.")

    elif select == 4:
        print("전화번호 삭제 기능입니다. \n삭제할 이름을 입력해주세요(ex.인천_김재현).")
        name = input("이름: ")
        if name not in numLib:
            print("해당 이름을 찾을 수 없습니다.")
            continue
        del numLib[name]
        print("전화번호가 삭제되었습니다.")

    else:
        print("올바른 메뉴 번호를 입력해주세요.")
