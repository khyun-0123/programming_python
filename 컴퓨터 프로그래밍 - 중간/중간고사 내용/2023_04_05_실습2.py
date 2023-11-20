num = int(input("숫자를 입력 ==> "))

signal = 0
three = 0
seven = 0

if (num % 3 == 0):
    three = 1


if (num % 7 == 0):
    seven = 1

signal = three + seven

if (signal == 2):
     print ('"3의 배수 이면서 7의 배수"')
else:
    if (signal ==1):
        if (three == 1):
            print ('"3의 배수"')
        if (seven == 1):
            print ('"7의 배수"')
    else:
        print('"3의 배수도 7의 배수도 아닙니다."')
