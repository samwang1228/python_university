import tkinter as tk
import random
from random import choice
# min_value = int(min_en.get())#get的type是str
# max_value = int(max_en.get())
#   j=min_value
#  while (j<=max_value):
#         value2.append(j)
#         j=j+1
#     data = choice(value2)
#     value2.remove(data)
#import pypercilp 有copy Label 函式可用
win = tk.Tk() #建立視窗
win.title("抽獎就是棒")
win.geometry("500x400+400+100") #+x +y
win.config(bg="#323232")
lb = tk.Label(text="抽獎產生器", fg="skyblue",bg="#323232")  #建立文字 fg為字體顏色
lb.config(font="微軟正黑體 24")
lb.pack()  #注意出現的順序由pack決定
min_range = tk.Label(text="最小號碼", fg="white", bg="#323232")
min_range.config(font="微軟正黑體 15")
min_range.pack()
min_en = tk.Entry()
min_en.pack()
value_show = tk.Label(text="", fg="white", bg="#323232")
value_show.config(font="微軟正黑體 15")    
max_range = tk.Label(text="最大號碼", fg="white", bg="#323232")
max_range.config(font="微軟正黑體 15")
max_range.pack()
max_en = tk.Entry()
max_en.pack()

# counter=1
number = tk.Label(text="人數", fg="white", bg="#323232")
number.config(font="微軟正黑體 15")
number.pack()
number_input = tk.Entry()
number_input.pack()

def min_ran():
    value2 = []
    value = []
    min_value = int(min_en.get()) #get的type是str
    max_value = int(max_en.get())
    j=min_value
    while (j<=max_value):
        value2.append(j)
        j = j + 1
    
    n = int(number_input.get())
    value = ["中獎號碼為:"]
    count=0
    for i in range(n):
        if (count == 9):
            value.append("\n         ")
            count = 0
        count = count + 1
        data = choice(value2)
        value.append(data)
        value2.remove(data)
    value_show.config(text=value)

btn = tk.Button(text="確認", command=min_ran)


btn.config(font="微軟正黑體 15")
btn.pack()
value_show.pack()
win.mainloop()#不斷執行的意思 像是視窗要一直開