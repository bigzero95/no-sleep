#https://m.blog.naver.com/amethyst_lee/222010340950 참고


import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("졸음 운전 방지 Gui")
root.geometry("540x380+200+100")

btn1 = Button(root, text="1단계")
btn1.pack()

btn2 = Button(root, padx=10, pady=10, text="2단계")
btn2.pack()

btn3 = Button(root, padx=10, pady=10, text="3단계")
btn3.pack()


def btncmd():
    print("버튼이 클릭")

btn4 = Button(root, padx=10, pady=10, text="동작단계", command=btncmd)
btn4.pack()

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "도착 소요 시간을 입력하세요")

ent = Entry(root, width=30)
ent.pack()
ent.insert(0,"00분: ")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")
def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")
def yesno():
    msgbox.askyesno("예/아니오")
def yesnocancel():
    msgbox.askyesnocancel(title=None, message="sd""예/아니오")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=yesno, text="경고 / 경고 / 경고").pack()
Button(root, command=yesnocancel, text="경고 / 경고 / 경고").pack()
root.mainloop()