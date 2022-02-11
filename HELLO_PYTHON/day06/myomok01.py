from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5.QtGui import QIcon


form_class = uic.loadUiType("myomok01.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.cnt = 0
        self.pb.clicked.connect(self.myclick)
    def myclick(self):
        self.cnt += 1
        self.pb.setIcon(QIcon("{}.png".format(self.cnt%3)))

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
