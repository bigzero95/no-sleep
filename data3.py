#출처: https://sh-itstory.tistory.com/category/it/python%28%ED%8C%8C%EC%9D%B4%EC%8D%AC%29  [개발자승학 블로그]


# 알람음을 재생하기 위한

# wave와 pygame 헤더를 추가합니다.

import wave 

import pygame



# 현재 시간을 1초단위로 가져오기 위한 getCurrentTime 모듈

import getCurrentTime

import threading

# 그래픽 사용자 인터페이스(GUI)를 사용하기 위한 모듈

from tkinter import *

from tkinter import ttk





# 파일 경로 지정

file_path = 'I:/mp3/alarm.wav'

file_wav = wave.open(file_path)





# TK 클래스의 생성자 호출

window = Tk()

str_hour = StringVar()

str_minute = StringVar()

str_hour.set(0)

str_minute.set(0)





# pygame으로 노래를 재생하면 delay가 생깁니다.

# delay를 없애고 원래의 노래 재생 속도로 재생합니다.

frequency = file_wav.getframerate()

pygame.mixer.init(frequency=frequency)

pygame.mixer.music.load(file_path)



# 현재시간을 계속 가져옵니다.

getCurrentTime.TaskCurrentTime()



# alarmFlag = 0  ==> alarm종료상태

# alarmFlag = 1  ==> alarm설정상태

alarmFlag = 0



def alarm_On():

    # 알람음을 재생합니다.

    pygame.mixer.music.play()



def alarm_Off():

    # 알람음을 중지합니다.

    pygame.mixer.music.stop()



# 현재시간과 알람시간을 계속 비교합니다.

def CheckTime():

    global alarmFlag

    timer = threading.Timer(3,CheckTime)     

    timer.start()

     

    realTime_Hour = getCurrentTime.hour

    realTime_Minute = getCurrentTime.minute

    myHour = int(str_hour.get())

    myMinute = int(str_minute.get())



    if(realTime_Hour == myHour and realTime_Minute == myMinute and alarmFlag == 1):    

        timer.cancel()   

        print(alarmFlag)

        alarm_On()



    if(alarmFlag == 0):

        print("알람음 종료합니다.")

        alarm_Off()     

   

class MyAlarm:

    def __init__(self):

        pass

    def alarmSet(self):

        global alarmFlag

        alarmFlag = 1

        CheckTime()

        

    def alarmReset(self):

        global alarmFlag

        alarmFlag = 0

        CheckTime()

       

window.geometry("350x150+150+50")

    

myAlarm = MyAlarm()

la = Label(window, text="시간 입력 ex 오전 8시 ==> 8 , 오후8시 ==> 20")

la.grid(column = 0 , row = 0)

textbox = ttk.Entry(window,width=10,textvariable = str_hour)

textbox.grid(column = 1 , row = 0)

la = Label(window, text="분 입력 ex 8분 ==> 8 , 58분 ==> 58")

la.grid(column = 0 , row = 1)

textbox2 = ttk.Entry(window,width=10,textvariable = str_minute)

textbox2.grid(column = 1 , row = 1)

btn_On = Button(window, text="알람설정", command=myAlarm.alarmSet)

btn_On.place(x=100,y=100)    

btn_Off = Button(window, text="알람해제", command=myAlarm.alarmReset)

btn_Off.place(x=200,y=100)



window.mainloop()