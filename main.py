
#import time

#def FUNCTIONS():
 #   max_time_end = time.time() + (60 * 1)
  #  while True:
   #     print("TEST")
    #    if time.time() > max_time_end:
     #       break
             
from playsound import playsound

import random
import time

playsound("방사능 위험 알람소리.mp3" ) 

x = int(input("도착 소요 시간 : "))
i = int(input("졸림 정도 : " ))  
counter = x
print ("졸음 방지 프로그램을 실행합니다.")

start_time = time.time()
while time.time() - start_time < counter:     
     if round(time.process_time()) == i:
          print(random.randint(0,100))  #랜덤 알람 대체
          time.sleep(1)

     #elif 
      #    n = input('졸림정도 : ')
       ## break



     
    



        


#import random
#import time
#import timetemp

#x = int(input('time(second) : '))

#my_num = 3
#counter = x

#start_time = time.time()
#while time.time() - start_time < counter:
 #    timetemp = time.time() - start_time
  #   if round(timetemp) == my_num:
   #       print(random.randint(0,100))
    #      time.sleep(3)
    
