#time은 초로 정의
time = int(input())    #366666

sec = time%60   
hour = time//3600
minute = time//60 - hour*60

print("%d시간 %d분 %d 초" % (hour, minute, sec) )
