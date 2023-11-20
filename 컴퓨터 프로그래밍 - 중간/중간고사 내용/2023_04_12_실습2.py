num = int(input("수를 입력해 주세요. : "))
output = ""
data = 0

for i in range (1, num+1):
    data += i
    output += str(i)
    output += "+"

output = output[:-1]
output = output + "=" + str(data)
print (output)