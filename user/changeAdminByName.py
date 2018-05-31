# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from .Ui_changeAdminByName import *
import pymysql

class chaneAdmin(QWidget, Ui_Form):
    signal_0=pyqtSignal()

    def __init__(self, updateState,  parent=None):    
        super(chaneAdmin, self).__init__(parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.updateState=updateState
            
        self.signal_0.connect(self.updateState)
        
        self.pushButton.clicked.connect(self.ok)
        
        self.pushButton_2.clicked.connect(self.cancel)
            
            
        
    def cancel(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
                
        
    def ok(self):
        id=self.lineEdit.text()    
        passwd=self.lineEdit_2.text()
        tele=self.lineEdit_3.text()
        email=self.lineEdit_4.text()
        
        
        db = pymysql.connect(host="67.209.xxx.xxx",user="root",passwd="xxxxxxxxxxx",db="db_sharedbike")
        cursor = db.cursor()
        
        sql='''update user_info set password='%s', phonenum='%s', email='%s'   WHERE username='%s' '''%( passwd,  tele,  email,  id)
        print(sql)
        return_num=0
        try:
            return_num=cursor.execute(sql)

        except Exception as e:
            #数据库连接发生错误
            QMessageBox.information(self,  "错误提示",  "输入错误")

            print ("Error: unable to fetch data")
            print (e)
        
        if(return_num==0):QMessageBox.information(self,  "错误提示",  "操作失败")
        
        if(return_num==1):QMessageBox.information(self,  "成功提示",  "操作成功")

        print(return_num)
        
        self.signal_0.emit()
        self.cancel()
        
        

            
            
            
            
            
            
            
