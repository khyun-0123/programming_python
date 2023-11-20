#여러 개의 명언을 리스트에 저장해 놓고, 저장된 명언을 랜덤하게 출력

import random

myungunList = []
myungunList.append('"실패는 재도전할 수 있는 기회다." - 헨리 포드')
myungunList.append('"오늘 거기에 있지 않은 것을 끝까지 추구하면, 내일은 거기에 도달할 수 있다." - 얀 라보셰')
myungunList.append('"우리가 마음으로 그리는 대로, 우리 삶은 그려진다." - 에머슨')

randomnum = random.randint(0,2)

print(myungunList[randomnum])