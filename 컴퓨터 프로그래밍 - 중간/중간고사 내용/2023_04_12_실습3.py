# for a in range (2, 10):
#     for b in range(1, 10):
#         print(a, "x", b, "=", a*b)
#     print("\n")

for a in range (1, 10):
    for b in range(2, 5):
        print("%d%s%d%s%2d" % (b, "x",  a, "=", b*a), end=' ')
        print('\t', end='')
    print("")