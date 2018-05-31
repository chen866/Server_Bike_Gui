# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_loginView import *
import pymysql
from QMain import QMain


class LoginMain(QWidget, Ui_Form):
    def __init__(self, parent=None):    
        super(LoginMain, self).__init__(parent)
        #self.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
        self.setupUi(self)
        

        self.pushButton.clicked.connect(self.cancel)
        self.pushButton_2.clicked.connect(self.ok)
        
        
    def ok(self): 
        name=self.lineEdit.text()
        passwd=self.lineEdit_2.text()
       
        db = pymysql.connect(host="67.209.xxx.xxx",user="root",passwd="xxxxxxxxxxxxx",db="db_sharedbike")
        cursor = db.cursor()
 
        sql="select passwd from admin where name='%s'"%(name)

        try:
            cursor.execute(sql)
            result=cursor.fetchone()

            print(result)
            
            if result==None:
                #没有改用户名
                print(0)
                self.cancel()
                QMessageBox.information(self,  "错误提示",  "没有该用户名")
            elif result[0]==passwd:
                #密码正确
                print(1)
                ###进入下一个界面
                self.close()
                self.qmain=QMain(name)
                self.qmain.show()
                
            else:
                #密码不正确
                print(2)
                self.cancel()
                QMessageBox.information(self,  "错误提示",  "数据库连接失败")
        except Exception as e:
            #数据库连接发生错误
            QMessageBox.information(self,  "错误提示",  "密码不正确")

            print ("Error: unable to fetch data")
            print (e)
     
    
    def cancel(self):   
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

            
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin2 = LoginMain()  
    myWin2.show()  
    sys.exit(app.exec_())  
