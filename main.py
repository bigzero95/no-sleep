
#import time

#def FUNCTIONS():
 #   max_time_end = time.time() + (60 * 1)
  #  while True:
   #     print("TEST")
    #    if time.time() > max_time_end:
     #       break
             
from pygame import mixer
import os
import random
import time
import pygame

path = "C:\\Users\\AimToG\\Downloads\\졸음운전방지\\random_sound"

x = int(input("도착 소요 시간(00분) : "))
x_2 = x*60

i = int(input("졸림 정도(1~3단계) : " ))  
i_2 = i*6

#while i <= 1111 :
 #    if (i>=1 and i<=3) : 
  #        print ("졸음 방지 프로그램을 실행합니다.")
   #       break
    # else :
     #     print ("잘못된 입력입니다.")
      #    continue

while i>=1 and i<=3 :
     print ("졸음 방지 프로그램을 실행합니다.")
     break
     if i<=0 and i>=4 :
          print ("잘못된 입력입니다.")
          continue

start_time = time.time()
while time.time() - start_time < x_2:      
     if round(time.process_time()) == i_2:
          print ("졸음 방지 알람입니다. 종료하시려면 버튼을 누르세요")
          soundtrack = os.path.join(path, random.choice(os.listdir(path)))
          pygame.mixer.init()
          pygame.mixer.music.load(soundtrack)
          pygame.mixer.music.play(-1)
          i = int(i)+int(input("졸림 정도(1~3단계) : " ))
          i_2 = i*6
          pygame.mixer.music.stop()
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
    
