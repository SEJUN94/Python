from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import pyautogui as pg


form_class = uic.loadUiType("pymain09.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb1.clicked.connect(self.myclick1)
        self.pb2.clicked.connect(self.myclick2)
        self.pb3.clicked.connect(self.myclick3)
        self.pb4.clicked.connect(self.myclick4)
        self.pb5.clicked.connect(self.myclick5)
        self.pb6.clicked.connect(self.myclick6)
        self.pb7.clicked.connect(self.myclick7)
        self.pb8.clicked.connect(self.myclick8)
        self.pb9.clicked.connect(self.myclick9)
        self.pb0.clicked.connect(self.myclick0)
        self.pbCall.clicked.connect(self.myclick)
        
        
    def myclick(self):
        z = self.le.text()
        #messagebox.showinfo("연결중",z+"에게 연결중 입니다.")
        #a = pg.alert(text=z+'에게 연결중 입니다.', title='연결중', button='OK')
        a = pg.confirm(text=z+'에게 연결중 입니다.', title='연결중', buttons=['OK', 'Cancel'])
        print(a)
        #pyautogui.alert(z+'에게 연결중 입니다.')
        
    def myclick1(self):
        a = self.pb1.text()
        z = self.le.text()
        self.le.setText(z+a)
    
    def myclick2(self):
        b = self.pb2.text()
        z = self.le.text()
        self.le.setText(z+b)
    
    def myclick3(self):
        c = self.pb3.text()
        z = self.le.text()
        self.le.setText(z+c)
        
    def myclick4(self):
        d = self.pb4.text()
        z = self.le.text()
        self.le.setText(z+d)
    
    def myclick5(self):
        e = self.pb5.text()
        z = self.le.text()
        self.le.setText(z+e)
    
    def myclick6(self):
        f = self.pb6.text()
        z = self.le.text()
        self.le.setText(z+f)   
        
    def myclick7(self):
        g = self.pb7.text()
        z = self.le.text()
        self.le.setText(z+g)
    
    def myclick8(self):
        h = self.pb8.text()
        z = self.le.text()
        self.le.setText(z+h)
    
    def myclick9(self):
        i = self.pb9.text()
        z = self.le.text()
        self.le.setText(z+i)  
        
    def myclick0(self):
        j = self.pb0.text()
        z = self.le.text()
        self.le.setText(z+j)
     
               
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
