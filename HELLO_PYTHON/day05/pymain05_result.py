import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication



form_class = uic.loadUiType("pymain05.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        arr45= [
                1,2,3,4,5,      6,7,8,9,10,
                11,12,13,14,15, 16,17,18,19,20,
                21,22,23,24,25, 26,27,28,29,30,
                31,32,33,34,35, 36,37,38,39,40,
                41,42,43,44,45
            ]     
        arr6 = []
        
        while len(arr6) < 6 :
            rnd = int(random.random()*45)
            if arr45[rnd] > 0:
                arr6.append(arr45[rnd])
                arr45[rnd] = -1
            else:
                continue
            
        for i in range(6):
            for j in range(6):
                if arr6[i] < arr6[j]:
                    a = arr6[i]
                    b = arr6[j]
                    arr6[i] = b
                    arr6[j] = a
            
        # for i in range(len(arr6) - 1, 0, -1):
        #     swapped = False
        #     for j in range(i):
        #         if arr6[j] > arr6[j + 1]:
        #             arr6[j], arr6[j + 1] = arr6[j + 1], arr6[j]
        #             swapped = True
        #     if not swapped:
        #         break
            
        print(arr6)
        
        self.le1.setText(str(arr6[0]))        
        self.le2.setText(str(arr6[1]))        
        self.le3.setText(str(arr6[2]))        
        self.le4.setText(str(arr6[3]))        
        self.le5.setText(str(arr6[4]))        
        self.le6.setText(str(arr6[5]))    
    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
