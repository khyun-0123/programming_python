# myList = ["이", "진", "희"]
# a = ((myList[0]+myList[1]+myList[2]+" ")*4)
# print(a)
# myList[0] = "김"
# a = ((myList[0]+myList[1]+myList[2]+" ")*4)
# print(a)


s = "이진희 이진희 이진희"



for i in range(len(s)):

    if(s[i] == '이'):

        print("김", end = '')

    else:

        print(s[i], end = '')