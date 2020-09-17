from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QLineEdit,QFont
import sys
class Caculator(QWidget):
    def __init__(self):
            super().__init__()
            self.Set_Ui()
    def Set_Ui(self):
        # self.setGeometry(500,500,400,300)
        self.result_text=""
        self.out=""
        self.clc_temp=-1
        self.resize(400, 240)
        self.bt_str=["C","÷","×","7","8","9","4","5","6","1","2","3","%","0","."]
        self.bt=[]
        #设置显示框
        self.result=QLabel(self)
        self.result.setGeometry(0,0,400,40)
        self.result.setStyleSheet("background-color:#000000;color:#ffffff")
        self.result.setFont(QFont("Timer",20,QFont.Bold))
        self.setStyleSheet("background:black")

        self.bt_style = "background:black;color:white;border: 1px solid #eeeeee"
        #设置按钮
        self.Font = QFont("Timer", 20, QFont.Bold)
        for i in self.bt_str:
            self.bt.append(QPushButton(i,self))

        for i in range(len(self.bt)):
            # for j in range(5):
                self.bt[i].setGeometry((i%3)*100,40*(int(i/3)+1),100,40)
                self.bt[i].setStyleSheet(self.bt_style)
                self.bt[i].setFont(self.Font)
        self.bt[0].clicked.connect(self.clc)
        self.bt[1].clicked.connect(lambda: self.click_bt(self.bt[1]))
        self.bt[2].clicked.connect(lambda: self.click_bt(self.bt[2]))
        self.bt[3].clicked.connect(lambda: self.click_bt(self.bt[3]))
        self.bt[4].clicked.connect(lambda: self.click_bt(self.bt[4]))
        self.bt[5].clicked.connect(lambda: self.click_bt(self.bt[5]))
        self.bt[6].clicked.connect(lambda: self.click_bt(self.bt[6]))
        self.bt[7].clicked.connect(lambda: self.click_bt(self.bt[7]))
        self.bt[8].clicked.connect(lambda: self.click_bt(self.bt[8]))
        self.bt[9].clicked.connect(lambda: self.click_bt(self.bt[9]))
        self.bt[10].clicked.connect(lambda: self.click_bt(self.bt[10]))
        self.bt[11].clicked.connect(lambda: self.click_bt(self.bt[11]))
        self.bt[12].clicked.connect(lambda: self.click_bt(self.bt[12]))
        self.bt[13].clicked.connect(lambda: self.click_bt(self.bt[13]))
        self.bt[14].clicked.connect(lambda: self.click_bt(self.bt[14]))


        self.clc_bt1 = QPushButton("DEL", self)
        self.clc_bt1.setGeometry(300, 40, 100, 40)
        self.clc_bt1.setStyleSheet(self.bt_style)
        self.clc_bt1.setFont(self.Font)
        self.clc_bt1.clicked.connect(self.delet)


        self.clc_bt2 = QPushButton("-", self)
        self.clc_bt2.setGeometry(300, 80, 100, 40)
        self.clc_bt2.setStyleSheet(self.bt_style)
        self.clc_bt2.setFont(self.Font)
        self.clc_bt2.clicked.connect(lambda: self.click_bt(self.clc_bt2))

        self.clc_bt3 = QPushButton("+", self)
        self.clc_bt3.setGeometry(300, 120, 100, 40)
        self.clc_bt3.setStyleSheet(self.bt_style)
        self.clc_bt3.setFont(self.Font)
        self.clc_bt3.clicked.connect(lambda :self.click_bt(self.clc_bt3))

        self.clc_bt4 = QPushButton("=", self)
        self.clc_bt4.setGeometry(300, 160, 100, 80)
        self.clc_bt4.setStyleSheet(self.bt_style)
        self.clc_bt4.setFont(self.Font)
        self.clc_bt4.clicked.connect(self.caculat)

        self.setWindowTitle("Caculator")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()
    def click_bt(self,bt):
        self.result_text+=bt.text()
        self.result.setText(self.result_text)
    def caculat(self):
        try:
            ss=self.result_text.replace("×", "*").replace("÷", "/")
            ss=self.process(ss).replace("%","/100")
            print(ss)
            self.out=self.result_text+"="+str(eval(ss))
        except:
            self.out="Error!!"
        self.result.setText(self.out)
        self.result_text = ""
    def clc(self):
        self.clc_temp = -1
        self.result_text=""
        self.out=""
        self.result.setText("")
    def delet(self):
        if len(self.result_text)>0:
            self.result_text=self.result_text[0:-1]
            self.result.setText(self.result_text)
    def process(self,string):
        str_list=["%0","%1","%2","%3","%4","%5","%6","%7","%8","%9"]
        for s in str_list:
            string=string.replace(s,"/100*"+s[1])
        return string

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Caculator()
    sys.exit(app.exec_())

