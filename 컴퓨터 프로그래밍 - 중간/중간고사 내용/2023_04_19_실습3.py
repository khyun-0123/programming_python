sum = 0
count = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    sum += i
    count += 1
print("짝수의 개수는", count, "짝수 합은", sum)