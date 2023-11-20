#영어사전 만들기, 딕셔너리로
eng_dict = {"flower" : "꽃",
         "fruit" : "과일",
         "food" : "음식"
         "water : 물"
         "desk : 책상"}

while True:
    finding = input("찾을 단어: ")
    if finding == "quit":
        break
    else:
        print(eng_dict.get(finding))