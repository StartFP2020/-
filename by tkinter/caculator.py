# 作者：王洪
# 日期：2020.08.10
from tkinter import *
from tkinter import messagebox
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.sentence=[]
        self.status=False
        self.var=StringVar()
        self.var1=StringVar()
        self.master.geometry("192x200")
        self.master.resizable(0,0)
        self.master.title("计算器")
        self.init_Button()
        self.init_entry()
    def init_Button(self):
        self.bt1 = Button(text="+",command=lambda:self.caculate(self.bt1["text"]),width=3,height=1,font=('Helvetica', '12'))
        self.bt2 = Button(text="-", command=lambda:self.caculate(self.bt2["text"]),width=3,height=1,font=('Helvetica', '12'))
        self.bt3 = Button(text="*", command=lambda:self.caculate(self.bt3["text"]),width=3,height=1,font=('Helvetica', '12'))
        self.bt4 = Button(text="/", command=lambda:self.caculate(self.bt4["text"]),width=3,height=1,font=('Helvetica', '12'))
        self.bt5 = Button(text="(", command=lambda: self.caculate(self.bt5["text"]), width=3, height=1,font=('Helvetica', '12'))
        self.bt6 = Button(text=")", command=lambda: self.caculate(self.bt6["text"]), width=3, height=1,font=('Helvetica', '12'))
        self.bt1.grid(row=0, column=4)
        self.bt2.grid(row=1, column=4)
        self.bt3.grid(row=2, column=4)
        self.bt4.grid(row=3, column=4)
        self.bt5.grid(row=3, column=0)
        self.bt6.grid(row=3, column=2)
        self.bt_del = Button(text="清除", command=lambda:self.clear_out(),width=3,height = 3,font=('Helvetica', '12'))
        self.bt_clear = Button(text="删除", command=lambda:self.del_sen(),width=3, height = 3,font=('Helvetica', '12'))
        self.bt_equal = Button(text="=", command=lambda:self.caculate_out(),width=12, height=1, font=('Helvetica', '12'))
        self.bt_point = Button(text=".", command=lambda: self.caculate("."), width=7, height=1, font=('Helvetica', '12'))
        self.bt_del.grid(row=0, column=5, rowspan=2)
        self.bt_clear.grid(row=2, column=5, rowspan=2)
        self.bt_equal.grid(row=4, column=0,columnspan=3)
        self.bt_point.grid(row=4, column=4,columnspan=2)
        self.bt_num=[]
        # for i in range(10):
        self.bt_num.append(Button(text=str(0),command=lambda:self.caculate(str(0)),width=3,height=1,font=('Helvetica', '12')))
        self.bt_num.append(Button(text=str(1), command=lambda: self.caculate(str(1)), width=3, height=1, font=('Helvetica', '12')))
        self.bt_num.append(Button(text=str(2), command=lambda: self.caculate(str(2)), width=3, height=1, font=('Helvetica', '12')))
        self.bt_num.append(Button(text=str(3), command=lambda: self.caculate(str(3)), width=3, height=1, font=('Helvetica', '12')))
        self.bt_num.append(Button(text=str(4), command=lambda: self.caculate(str(4)), width=3, height=1, font=('Helvetica', '12')))
        self.bt_num.append(Button(text=str(5), command=lambda: self.caculate(str(5)), width=3, height=1, font=('Helvetica', '12')))
        self.bt_num.append(Button(text=str(6), command=lambda: self.caculate(str(6)), width=3, height=1, font=('Helvetica', '12')))
        self.bt_num.append(Button(text=str(7), command=lambda: self.caculate(str(7)), width=3, height=1, font=('Helvetica', '12')))
        self.bt_num.append(Button(text=str(8), command=lambda: self.caculate(str(8)), width=3, height=1, font=('Helvetica', '12')))
        self.bt_num.append(Button(text=str(9), command=lambda: self.caculate(str(9)), width=3, height=1, font=('Helvetica', '12')))
        for j in range(0,9):
            self.bt_num[j+1].grid(row=int(j/3), column=j%3)
        self.bt_num[0].grid(row=3, column=1)
    def init_entry(self):
        self.e1=Entry(textvariable=self.var,width=20,font=('Helvetica', '12')).grid(row=7,column=0,columnspan=6)
    def caculate(self,s):
        if self.status:
            self.sentence=[]
        self.sentence.append(s)
        self.var.set("".join(self.sentence))
        self.status=False
    def del_sen(self):
        if len(self.sentence)!=0:
            self.sentence.pop()
        self.var.set("".join(self.sentence))
    def caculate_out(self):
        if len(self.sentence)!=0:
            try:
                out=eval("".join(self.sentence))
                self.var.set("".join(self.sentence) + "=" + str(out))
                self.status = True
            except:
                messagebox.showinfo("警告","表达式错误")
    def clear_out(self):
        self.sentence = []
        self.var.set("".join(self.sentence))
if __name__=="__main__":
    tk=Tk()
    myapp=App(tk)
    myapp.mainloop()
