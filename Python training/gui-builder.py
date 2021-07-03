from tkinter import *
from tkinter import messagebox
import subprocess as sub

class start:
    def __init__(self):
        self.user_obj = []
        self.op = Tk()
        self.op.title("視窗元件")
        self.op.geometry("300x580+0+80")
        self.mainwin = Tk()
        self.mainwin.title("main window")
        self.mainwin.geometry("700x600+310+80")
        self.cfg = Tk()
        self.cfg.title("config")
        self.cfg.geometry("300x600+1020+80")
        self.view_mouse()
        self.create_content()
        self.build_window()

    def view_mouse(self):
        self.user_x, self.user_y = 0, 0
        self.var = StringVar()
        self.var.set("x: {}, y: {}".format(self.user_x, self.user_y))
        self.mainwin.bind("<Motion>", self.mouse)

    def mouse(self, event):
        self.user_x, self.user_y = event.x, event.y
        self.var.set(f"x: {self.user_x}, y: {self.user_y}")

    def created(self, event):
        try:
            vars(self)[self.obj_n.get()] = Label(self.mainwin, text=self.obj_n.get(), fg="black") if self.obj == "label" else Button(self.mainwin, text=self.obj_n.get(), bg="white", fg="black") if self.obj == "button" else Entry(self.mainwin,bg="white",fg="black") if self.obj == "entry" else Checkbutton(self.mainwin, text=self.obj_n.get()) if self.obj == "checkbutton" else Radiobutton(self.mainwin, text=self.obj_n.get())
            eval("self."+self.obj_n.get()).place(x=self.user_x, y=self.user_y)
            self.user_obj.append(self.obj_n.get())
        except:
            messagebox.showerror("Error", "請定義變數或換個名稱")
            
            # AttributeError 為定義數

    def close(self):
        self.op.destroy()
        self.mainwin.destroy()
        self.cfg.destroy()

    def ready_for_create(self, obj):
        self.now_layout["text"] = obj.title()
        self.obj = obj
    
    def build_window(self):
        self.op.mainloop()
        self.mainwin.mainloop()
        self.cfg.mainloop()

    def change(self):
        # eval("self."+self.user_obj_name.get())[""]
        try:
            eval("self."+self.user_obj_name.get())["text"] = self.user_obj_text.get()
        except:
            pass
        try:
            eval("self."+self.user_obj_name.get())["fg"] = self.user_obj_fg.get()
        except SyntaxError:
            pass
        except AttributeError: # 為定義變數
            print("att")
        except:
            pass
        try:
            eval("self."+self.user_obj_name.get())["bg"] = self.user_obj_bg.get()
        except SyntaxError:
            eval("self."+self.user_obj_name.get())["bg"] = None
        except AttributeError:
            print("att")
        except:
            pass

    def delete(self):
        eval("self."+self.want_del.get()).place_forget()
        self.user_obj.remove(self.want_del.get())
        vars(self)[self.want_del.get()] = None

    def save(self, name):
        with open(f"{name}.txt", "w", encoding="utf-8") as self.file:
            self.file.write("from tkinter import *\n\n")
            self.file.write(f"tk = Tk()\ntk.geometry(\"{self.mainwin.winfo_width()}x{self.mainwin.winfo_height()}\")\n")
            # ======= main =======
            for i in self.user_obj:
                # eval("self."i)["text"]
                if eval("self."+i).winfo_class() != "Entry":
                    self.file.write(f"{i} = {eval('self.'+i).winfo_class()}(tk, text='{eval('self.'+i)['text']}', fg='{eval('self.'+i)['fg']}', bg='{eval('self.'+i)['bg'] if  eval('self.'+i)['bg'] != None else None}')\n")
                else:
                    self.file.write(f"{i} = Entry(tk)\n")
                    
                self.file.write(f'{i}.place(x={eval("self."+i).winfo_x()}, y={eval("self."+i).winfo_y()})\n')
            self.file.write("tk.mainloop()")
            # ======= main =======
        sub.run(f"rename {name}.txt {name}.py", shell=True)  # final
        self.open_file = messagebox.askquestion("是否開啟", "是否現在開啟你的檔案?")
        if self.open_file == 'yes':
            sub.run(f"python {name}.py")
    # ============================================

    def how_create(self):
        messagebox.showinfo("How to create layout?", "1. 為你想要的元件取名字\n2. 點擊想要的元件\n3. 讓\"視窗元件\"這個視窗變成焦點視窗，並且在\"main window\"裡滑動鼠標選擇自己想要的位置\n4. 按Enter")

    def how_change(self):
        messagebox.showinfo("How to change layout?", "1. 輸入你想更改的元件名稱\n2. 輸入想更改的內容\n3. 按下\"更改\"")

    def how_del(self):
        messagebox.showinfo("How to delete layout?", "1. 輸入想要刪除的名稱(不是text)\n2. 點擊\"刪除\"\n")
    
    def call_me(self):
        messagebox.showinfo("", "我的E-MAIL: wuj20061224@gmail.com\n如果有任何問題請找我")

    # ============================================

    def create_content(self):
        self.menu = Menu(self.op)
        self.op.config(menu=self.menu)
        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="操作說明", menu=self.helpmenu)
        self.helpmenu.add_command(label="放置元件", command=self.how_create)
        self.helpmenu.add_command(label="更改內容", command=self.how_change)
        self.helpmenu.add_command(label="刪除元件", command=self.how_del)
        self.usual = Menu(self.menu)
        self.menu.add_cascade(label="常見問題", menu=self.usual)
        self.usual.add_command(label="出現錯誤", command=self.call_me)
        Button(self.op, border=0, text="Label", width=10, bg="skyblue", command=lambda: self.ready_for_create("label")).pack(pady=10)
        Button(self.op, border=0, text="Button", width=10, bg="skyblue", command=lambda: self.ready_for_create("button")).pack(pady=10)
        Button(self.op, border=0, text="Entry", width=10, bg="skyblue", command=lambda: self.ready_for_create("entry")).pack(pady=10)
        Button(self.op, border=0, text="Checkbutton", width=10, bg="skyblue", command=lambda: self.ready_for_create("checkbutton")).pack(pady=10)
        Button(self.op, border=0, text="Radiobutton", width=10, bg="skyblue", command=lambda: self.ready_for_create("radiobutton")).pack(pady=10)
        Label(self.op, text="Object Name").pack()
        Label(self.op, text="↓", font=("bold", 16)).pack(pady=5)
        self.now_layout = Label(self.op, text="none")
        self.now_layout.pack()
        self.obj_n = Entry(self.op)
        self.obj_n.pack()
        Label(self.op, text="your x, y").pack(pady=5)
        Label(self.op, text="↓", font=("", 16)).pack(pady=5)
        Label(self.op, textvariable=self.var).pack()
        self.op.bind("<Return>", self.created)
        Label(self.op, text="If you want to create, press Enter.\n(在\"視窗元件\"上按Enter)").pack()
        Button(self.op, text="關閉這個程式", command=self.close).pack(pady=20)
        #================= config window ========================================
        Label(self.cfg, text="視窗元件管理", font=('微軟正黑體', 15)).grid(row=0, column=0, padx=80, columnspan=2)
        Label(self.cfg, text="元件名稱: ", font=('微軟正黑體', 13)).grid(row=1, column=0, pady=10)
        self.user_obj_name = Entry(self.cfg)
        self.user_obj_name.grid(row=1, column=1, sticky=W, pady=10)
        Label(self.cfg, text="文字(text):", font=('微軟正黑體', 13)).grid(row=2, column=0,pady=10)
        self.user_obj_text = Entry(self.cfg, fg="blue")
        self.user_obj_text.grid(row=2, column=1, sticky=W)
        Label(self.cfg, text="文字顏色:", font=('微軟正黑體', 13)).grid(row=3, column=0,pady=10)
        self.user_obj_fg = Entry(self.cfg, fg="green")
        self.user_obj_fg.grid(row=3, column=1, sticky=W)
        Label(self.cfg, text="背景顏色:", font=('微軟正黑體', 13)).grid(row=4, column=0,pady=10)
        self.user_obj_bg = Entry(self.cfg, fg="red")
        self.user_obj_bg.grid(row=4, column=1, sticky=W)
        Label(self.cfg, text="--------->").grid(row=5, column=0)
        Button(self.cfg, text='更改', command=self.change, border=0, bg="skyblue", fg="black", width=10).grid(row=5, column=1, sticky=W)
        Label(self.cfg, text="="*27, font=('', 13)).grid(row=6, column=0, columnspan=2)
        Label(self.cfg, text="刪除", font=('微軟正黑體', 15)).grid(row=7, column=0, columnspan=2, pady=10)
        Label(self.cfg, text="元件名稱: ", font=('微軟正黑體', 13)).grid(row=8, column=0, pady=10)
        self.want_del = Entry(self.cfg)
        self.want_del.grid(row=8, column=1, sticky=W)
        Label(self.cfg, text="--------->").grid(row=9, column=0)
        Button(self.cfg, text='刪除', command=self.delete, border=0, bg="skyblue", fg="black", width=10).grid(row=9, column=1, sticky=W)
        Label(self.cfg, text="="*27, font=('', 13)).grid(row=10, column=0, columnspan=2)
        Label(self.cfg, text="存檔", font=('微軟正黑體', 15)).grid(row=11, column=0, columnspan=2, pady=10)
        Label(self.cfg, text="File name:").grid(row=12, column=0)
        self.file_name = Entry(self.cfg, fg="blue")
        self.file_name.grid(row=12, column=1, sticky=W)
        Label(self.cfg, text="甭打副檔名").grid(row=13, column=0, columnspan=2)
        Button(self.cfg, text="存檔", fg="white", bg="#34eb7a", font=('微軟正黑體', 13), border=0, command=lambda:self.save(self.file_name.get())).grid(row=14, column=0, columnspan=2, pady=20)


t = start()

"""
微軟正黑體
get layout type: layoutName.winfo_class()
get window width: self.mainwin.winfo_width()
get window height: self.mainwin.winfo_height()
"""