num = int(input("값을 입력해주세요."))
data = 1
output = ""

for i in range (1, num+1):
    data = data * i
    num_2 = str(num - i + 1)
    output += num_2
    output += "*"

output = output[:-1]
output = str(num) + "!=" + output + "=" + str(data)
print(output)