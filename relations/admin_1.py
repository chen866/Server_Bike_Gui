# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from .Ui_admin_1 import *
from .DataGrid import DataGrid

class Order_1(QWidget, Ui_Form):
    def __init__(self, parent=None):    
        super(Order_1, self).__init__(parent)
        self.setupUi(self)
        

        self.pushButton.clicked.connect(self.cancel)
        self.pushButton_2.clicked.connect(self.ok)
        
    def cancel(self):
        self.lineEdit.setText("")
   
    def ok(self):
        input_num=self.lineEdit.text()
        try:
            x=int(input_num)
        except Exception as e:
            print("输入类型不对")
            QMessageBox.information(self,  "输入类型不对",  "输入类型不对，请重新输入！")
            self.lineEdit.setText("")
            return
            
            
        self.datagrid=DataGrid(input_num) 
        self.datagrid.show()        

if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin2 = Admin_1()  
    myWin2.show()  
    sys.exit(app.exec_())          
