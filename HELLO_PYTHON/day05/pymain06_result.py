import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


form_class = uic.loadUiType("pymain06.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        dan = self.le.text()
        idan = int(dan)
        txt = ""
        txt += "{}*{}={}\n".format(idan,1,idan*1)
        txt += "{}*{}={}\n".format(idan,2,idan*2)
        txt += "{}*{}={}\n".format(idan,3,idan*3)
        txt += "{}*{}={}\n".format(idan,4,idan*4)
        txt += "{}*{}={}\n".format(idan,5,idan*5)
        txt += "{}*{}={}\n".format(idan,6,idan*6)
        txt += "{}*{}={}\n".format(idan,7,idan*7)
        txt += "{}*{}={}\n".format(idan,8,idan*8)
        txt += "{}*{}={}\n".format(idan,9,idan*9)
        self.te.setText(txt)     
          
            
    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
