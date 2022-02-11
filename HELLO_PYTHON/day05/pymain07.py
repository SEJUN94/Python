from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import random
from _ast import Or

form_class = uic.loadUiType("pymain07.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)
        self.leMine.returnPressed.connect(self.myclick)
        
        
    def myclick(self):
        com = ""
        mine = ""
        result = ""
        
        mine = self.leMine.text()
        rnd = random.random()
        if rnd<0.33:
            com = "가위"
        elif rnd<=0.66:
            com = "바위"
        elif rnd<=1:
            com = "보"
            
        
        if com == mine: 
            result = "비김"
            
        elif mine in "가위" and com in "보" or mine in "바위" and com in "가위" or mine in "보" and com in "바위":
            result = "이김"
        elif mine in "가위" and com in "바위" or mine in "바위" and com in "보" or mine in "보" and com in "가위":
            result = "짐"
        
        
        self.leCom.setText(com)        
        self.leResult.setText(result)
    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
