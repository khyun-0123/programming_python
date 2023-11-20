#12345 별 찍기
a = 1
for i in range (5):
    b = (10-a)//2
    print(" "*b, end='')
    for i in range(a):
        print("*", end='')
    print(" "*b)
    a = a + 2

#54321 별 찍기
a = 9
for i in range (5):
    b = (10-a)//2
    print(" "*b, end='')
    for i in range(a):
        print("*", end='')
    print(" "*b)
    a = a - 2