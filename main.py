
#import time

#def FUNCTIONS():
 #   max_time_end = time.time() + (60 * 1)
  #  while True:
   #     print("TEST")
    #    if time.time() > max_time_end:
     #       break
             
from pygame import mixer

import random
import time
import pygame


x = int(input("도착 소요 시간 : "))
i = int(input("졸림 정도 : " ))  

print ("졸음 방지 프로그램을 실행합니다.")

start_time = time.time()
while time.time() - start_time < x:      
     if round(time.process_time()) == i:
          print ("버튼을 누르시오")
          pygame.mixer.init()
          pygame.mixer.music.load("C:\\Users\\AimToG\\Documents\\AlarmClockBell_S08HS.9.wav")
          pygame.mixer.music.play(-1)
          i = int(i)+int(input("졸림 정도 : " ))
          continue

#if i <= 3     
        

     #y = input('입력 : ' )

    # if y == ' ':
          #pygame.mixer.music.pause()
     #pygame.mixer.music.unpause()

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
    
