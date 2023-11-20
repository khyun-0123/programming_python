s="""나 보기가 역겨워
가실 때에는
말없이 고이 보내 드리오리다.

영변에 약산
진달래꽃
아름 따다 가실 길에 뿌리오리다.

가시는 걸음 걸음
놓인 그 꽃을
사뿐이 즈려 밟고 가시옵소서

나 보기가 역겨워 가실 때에는
죽어도 아니 눈물 흘리오리다."""

print("------------------------------")
print(s)
print("------------------------------")

print("\n")



k = str(input("찾을 문자를 입력해주세요: "))
time = s.count(k)
print("\n")
print(k, "이", time, "번 등장합니다.")

find = s.find(k)
print("찾은위치:",find, "번째")

length = len(k)

for i in range(time-1):
    find = find + length
    find = s.find(k,find)
    print("찾은위치:",find, "번째")
