a = 1

for i in range (5):
    b = (9-a)//2
    print(" "*b, end='')
    for i in range(a):
        print("*", end='')
    a = a + 2
    print("\n")