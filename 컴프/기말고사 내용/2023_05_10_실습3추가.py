starList = []
printList = []
for i in range (3):
    print(i+1, end='')
    starList.append(int(input("번째 줄에 별을 찍을 위치를 적어주세요. (1~3): ")))

for t in range (3):
    cnt = 3
    temp = starList[t]
    while True:
        if (temp == 1):
            printList.append("*")
            cnt -= 1
            break
        else:
            printList.append("O")
            temp -= 1
            cnt -= 1
    printList.append("O"*cnt)
    
for k in range (3):
    for i in range (3*k-3, 3*k):
        print(printList[i], end='')
    print()