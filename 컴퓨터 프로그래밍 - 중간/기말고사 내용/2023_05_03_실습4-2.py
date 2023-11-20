#교수님 풀이

name_ = ['a', 'b', 'c']
tel_ = ['01', '02', '03']

search_ = input("이름: ")

for i in range(0,3):
    if search_ == name_[i]:
        print("전화번호", tel_[i])