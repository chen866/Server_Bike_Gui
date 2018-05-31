# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from .Ui_changeAdmin import *
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
        self.lineEdit_5.setText("")
                
        
    def ok(self):
        id=self.lineEdit.text()    
        user_id=self.lineEdit_2.text()
        bike_id=self.lineEdit_3.text()
        start_time=self.lineEdit_4.text()
        over_time=self.lineEdit_5.text()

        
        
        db = pymysql.connect(host="67.209.xxx.xxx",user="root",passwd="xxxxxxxxx",db="db_sharedbike")
        cursor = db.cursor()
        
        sql='''update  order_info  set  user_id=%s,  bike_id=%s,  take_time='%s', return_time='%s'   WHERE id=%s'''%( user_id,  bike_id,  start_time,  over_time,  id)
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
        
        

            
            
            
            
            
            
            
