import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.Qt import QIcon, QSize


form_class = uic.loadUiType("myomok02.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        for j in range(10):
            for i in range(10):
                pb_one = QPushButton(self)
                pb_one.setText('')
                pb_one.setIcon(QIcon('0.png'))
                pb_one.setIconSize(QSize(40,40))
                pb_one.setGeometry(40*i,40*j,40,40)
                pb_one.clicked.connect(self.myclick)
    
    def myclick(self):
        btn = self.sender()
        print(btn.setIcon(QIcon('1.png')))

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
