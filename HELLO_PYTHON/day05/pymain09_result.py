from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from tkinter import messagebox
import pyautogui as pg
import pyautogui


form_class = uic.loadUiType("pymain09.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        self.pbCall.clicked.connect(self.myCall)
        
        
    def myclick(self):
        str_old = self.le.text()
        str_new = self.sender().text()
        self.le.setText(str_old+str_new)
        
    def myCall(self):
        z = self.le.text()
        #messagebox.showinfo("연결중",z+"에게 연결중 입니다.")
        QMessageBox.question(self, '연결중', z+'에게 연결중 입니다.', QMessageBox.Cancel, QMessageBox.NoButton)
        #a = pg.alert(text=z+'에게 연결중 입니다.', title='연결중', button='OK')
        #a = pg.confirm(text=z+'에게 연결중 입니다.', title='연결중', buttons=['OK', 'Cancel'])
        #print(a)
        #pyautogui.alert(z+'에게 연결중 입니다.')
               
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
