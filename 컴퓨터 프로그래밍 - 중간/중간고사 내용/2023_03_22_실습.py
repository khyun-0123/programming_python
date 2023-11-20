kor = int(input("국어 성적을 입력해주세요 : "))
eng = int(input("영어 성적을 입력해주세요 : "))
math = int(input("수학 성적을 입력해 주세요 : "))
total = kor + eng + math
mean = total/3
mean = ("%.2f" % (mean))
print ("총점은", total, "입니다.")
print ("평균은", mean, "입니다.")
