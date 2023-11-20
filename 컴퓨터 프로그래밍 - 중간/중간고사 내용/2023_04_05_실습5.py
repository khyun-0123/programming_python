import random

myHand = input("나의 가위/바위/보 ==> ")
comHand = random.choice(["가위", "바위", "보"])

print ("컴퓨터의 가위/바위/보 ==> ", comHand)

score = 0

if (myHand == "가위", comHand == "바위"):
    score =-1
if (myHand == "보", comHand == "가위"):
    score =-1
if (myHand == "바위", comHand == "보"):
    score =-1

if (myHand == "가위", comHand == "보"):
    score =+1

if (myHand == "보", comHand == "바위"):
    score =+1   

if (myHand == "바위", comHand == "가위"):
    score =+1

if (myHand == "가위", comHand == "가위"):
    score =0

if (myHand == "보", comHand == "보"):
    score =0

if (myHand == "바위", comHand == "바위"):
    score =0

if (score == 1):
    print("이겼습니다.")
if (score == -1):
    print("졌습니다.")
if (score == 0):
    print("비겼습니다.")

print("나의 승률은 ", score/3*100, "% 입니다.")