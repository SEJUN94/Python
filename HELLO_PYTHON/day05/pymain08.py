from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import random
from _ast import Or

form_class = uic.loadUiType("pymain08.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)
        
    def drawStar(self,cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"   
        return ret 
        
    def myclick(self):
        first = self.lefirst.text()
        last = self.lelast.text()
        
        ifirst = int(first)
        ilast = int(last)
        
        txt = ""
        for i in range(ifirst,ilast+1):
            txt += self.drawStar(i);print("ff")
        
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
