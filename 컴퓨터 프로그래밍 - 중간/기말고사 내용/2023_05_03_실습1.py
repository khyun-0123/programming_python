numList = []
hap = 0

for i in range (4):
    numList.append((int(input("숫자 입력: "))))
for i in range (4):
    hap += numList[i]
print("합계: ", hap)

#-----------------------------------------------------------

numList = [0, 0, 0, 0]
hap = 0

for i in range (0, 4):
    numList[i] = int(input("숫자: "))

for t in range(4):
    hap = hap + numList[t]

print(hap)