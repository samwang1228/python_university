#from tkinter import *
#這個方法的import可以直接使用函式名稱不用module.fuction
import tkinter as tk
win = tk.Tk() #建立視窗
win.title("視窗名稱")
def say():
    print("Hollo World")
img =tk.PhotoImage(file="C:\\Users\sam\Desktop\率.PNG") #記得要c:\\而非:\因為\u會讓python搞混
#btn = Button(text="start", bg="blue", width=5, height=7)  #建立一個名為start的Button bg=backgroud
btn = tk.Button(text="start")
#btn.config(width=99,height=99)
btn.config(image=img) #將buthon 得圖案設為圖片
#btn.config(bg="sktblue")#上面也可分開寫
btn.pack()  #讓你可以按
win.geometry("400x200")  #寬x高
btn.config(command=say) #當按下button執行say()
win.minsize(width=100, height=100)
win.maxsize(width=1024, height=1024)  #最大的限制
#win.resizable(False,False)#不能改變視窗大小
win.config(bg="skyblue")  #設定視窗顏色
win.attributes("-alpha", 1)  #讓視窗透明化RANGE 透明0~1清楚
win.attributes("-topmost",True)#至頂化 不會覆蓋視窗


win.mainloop()#不斷執行的意思 像是視窗要一直開