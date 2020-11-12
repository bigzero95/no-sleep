#출처: https://tre2man.tistory.com/188 [발자취]
#특정시간반복알고리즘

import time
import schedule
 
#특정 함수 정의
def printhello():
    print("Hello!")
 
 
schedule.every(30).minutes.do(printhello) #30분마다 실행
schedule.every().monday.at("00:10").do(printhello) #월요일 00:10분에 실행
schedule.every().day.at("10:30").do(job) #매일 10시30분에 
 
#실제 실행하게 하는 코드
while True:
    schedule.run_pending()
    time.sleep(1)




import time
import threading
 
#함수 정의, 함수 내부에 threading 정의
def printhello():
    print("Hello!")
    
    #threading을 정의한다. 5초마다 반복 수행함.
    threading.Timer(5, printhello).start()
 
#printhello 
printhello()

