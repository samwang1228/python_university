#from tkinter import *
#這個方法的import可以直接使用函式名稱不用module.fuction
import tkinter as tk
win = tk.Tk() #建立視窗
win.title("視窗名稱")
win.geometry("500x400+400+100") #+x +y
win.config(bg="skyblue")
lb = tk.Label(bg="skybLue", fg="black", text="This is lable!")  #建立文字 fg為字體顏色
lb.pack()#注意出現的順序由pack決定

def ok():
    t = en.get() #得到你打得字
    lb.config(text=t)

en = tk.Entry()#建立一個能打字的區塊
en.pack()
btn = tk.Button(text="ok",command=ok)
btn.pack()


win.mainloop()#不斷執行的意思 像是視窗要一直開