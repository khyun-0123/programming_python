var1 = input("첫 번쨰 문자열 ==> ")
var2 = input("두 번째 문자열 ==> ")

len1 = len(var1)
len2 = len(var2)

diff = len1 - len2

diff = abs(diff)

print("두 문자열의 차이는", diff, "입니다.")
