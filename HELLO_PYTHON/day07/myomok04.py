import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize
from pandas.tests.indexes.ranges.test_range import RI


form_class = uic.loadUiType("myomok04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flagWb = True
        self.flagEnd = False
        self.arr2D=[
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                                 
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                                 
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                                 
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
        ]
        self.pb2D = []
        
        
        for i in range(19):
            line = []
            for j in range(19):
                pb_one = QPushButton(self)
                pb_one.setText('')
                pb_one.setIcon(QIcon('0.png'))
                pb_one.setIconSize(QSize(40, 40))   
                pb_one.setGeometry(40*j,i*40, 40, 40)
                pb_one.clicked.connect(self.myclick)
                pb_one.setToolTip("{},{}".format(i,j))
                line.append(pb_one)
            self.pb2D.append(line)
        
        self.pb.clicked.connect(self.myreset)
        self.myrender()
    
    def myreset(self):
        for i in range(19):
            for j in range(19):
                self.arr2D[i][j]=0
        self.myrender()
        self.flagEnd = False
        self.flagWb = True
    
    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QIcon('2.png'))
        
    def myclick(self):
        if self.flagEnd:
            return 
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j]>0:
            return
        
        stone = -1
        if self.flagWb:
            self.arr2D[i][j]=1
            stone = 1
        else:
            self.arr2D[i][j]=2
            stone = 2
            
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        ri = self.checkRI(i,j,stone)
        le = self.checkLE(i,j,stone)
        ul = self.checkUL(i,j,stone)
        ur = self.checkUR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        dr = self.checkDR(i,j,stone)
        
        print("up",up)
        print("dw",dw)
        print("ri",ri)
        print("le",le)
        
        print("ul",ul)
        print("ur",ur)
        print("dl",dl)
        print("dr",dr)
        
        D1 = up + dw +1
        D2 = ur + dl +1
        D3 = le + ri +1
        D4 = ul + dr +1
        
        self.myrender()
        if D1 == 5 or D2 == 5 or D3 == 5 or D4 == 5:
            if self.flagWb:
                QMessageBox.question(self, 'OMOK','백돌승리', QMessageBox.Cancel, QMessageBox.NoButton)
            else:  
                QMessageBox.question(self, 'OMOK','흑돌승리', QMessageBox.Cancel, QMessageBox.NoButton)
            self.flagEnd = True
                
            
        
        self.flagWb = not self.flagWb
        
    def checkDR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt 
        except:
            return cnt 
        
        
    def checkDL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt 
        except:
            return cnt 
        
        
    def checkUR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt 
        except:
            return cnt 
        
        
    def checkUL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt 
        except:
            return cnt 
        
        
    def checkDW(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt 
        except:
            return cnt 
        
        
    def checkRI(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt 
        except:
            return cnt 
        
        
    def checkLE(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt 
        except:
            return cnt 
        
        
    def checkUP(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt 
        except:
            return cnt 
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    
    