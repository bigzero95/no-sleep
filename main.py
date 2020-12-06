
             
from pygame import mixer
import os
import random
import time
import pygame
from tkinter import *

path = "C:\\Users\\AimToG\\Downloads\\졸음운전방지\\random_sound"

x = int(input("도착 소요 시간(00분) : "))
x_2 = x*60
h = 5

while h <= 1111 :
     i = int(input("졸림 정도(1~3단계) : " ))  
     if (i>=1 and i<=3) : 
          print ("졸음 방지 프로그램을 실행합니다.")
          break
     else :
          print ("잘못된 입력입니다.")
          continue

i_2 = i*6
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

