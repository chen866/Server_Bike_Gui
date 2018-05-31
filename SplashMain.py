# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_splashView import *
from LoginMain import LoginMain

class SplashMain(QMainWindow, Ui_Form):
    def __init__(self, parent=None):    
        super(SplashMain, self).__init__(parent)
        self.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
        self.setupUi(self)
        
        self.time=5
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.countTime)
        self.timer.start(1000)
        
    def countTime(self):
        self.time-=1
        self.label_2.setText("还有"+str(self.time)+"秒跳转登入界面")
        if(self.time==0):
            self.close()
            self.myWin2 = LoginMain()  
            self.myWin2.show()  
            
            
            

            
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = SplashMain()  
    myWin.show()  
    sys.exit(app.exec_())  
