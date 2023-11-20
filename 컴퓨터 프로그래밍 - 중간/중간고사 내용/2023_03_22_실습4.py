jaryo = int(input("자료구조 성적은? : "))
soft = int(input("소프트개론 성적은? : "))
algo = int(input("알고리즘 성적은? : "))
avg = (jaryo + soft + algo)/3
if(avg>=60 and jaryo>=40 and soft>=40 and algo>=40):
    print ("합격")
else:
    print("불합격")
