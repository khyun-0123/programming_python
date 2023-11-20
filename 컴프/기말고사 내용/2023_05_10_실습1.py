test = []
re_test = []
cnt = 0

for t in range (10):
    print(t+1, end='')
    test.append(int(input("번째 사람 점수 입력: ")))
    
i = 0    
while True:
    if test[i] < 50:
        print(i+1, end='')
        test[i] = int(input("번째 사람 재시험 점수: "))
        re_test.append(i)
    else:
        i +=1
        if i >= 9:
            break
for k in range (10):
    cnt_temp = re_test.count(k)
    if cnt_temp>=1:
        cnt += 1

print("재시험 인원수: ", cnt)