# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_admin_2 import *
from DataGrid2 import DataGrid2

class Admin_2(QWidget, Ui_Form):
    def __init__(self, parent=None):    
        super(Admin_2, self).__init__(parent)
        self.setupUi(self)
        

        self.pushButton.clicked.connect(self.cancel)
        self.pushButton_2.clicked.connect(self.ok)
        
    def cancel(self):
        self.lineEdit.setText("")
   
    def ok(self):
        input_name=self.lineEdit.text()

            
            
        self.datagrid=DataGrid2(input_name) 
        self.datagrid.show()        

if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin2 = Admin_2()  
    myWin2.show()  
    sys.exit(app.exec_())          
