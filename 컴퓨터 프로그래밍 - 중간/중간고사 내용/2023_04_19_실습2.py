# 임의의 숫자 5개를 입력 받아서 합을 구하는 코딩, 이때 0이 들어오면 더 이상 입력받지 않고 합을 출력하고 종료.
num = 0
sum = 0
count = 0
for i in range (5):
    num = int(input("값 입력해주세요: "))
    count +=1
    if num == 0:
        break
    sum += num
print("입력 개수는", count, "개, 합계는", sum)