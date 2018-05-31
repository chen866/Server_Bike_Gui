# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_QMain import *
from admin_1 import *
from admin_2 import *
from addadmin import *
from DataGrid3 import *
from bike.bike import *
from bike.DataGridBike import *
from bike.addBike import *
from user.addadmin import *
from user.admin_1 import *
from user.admin_2 import *
from user.DataGrid3 import *
from relations.admin_1 import *
from relations.addadmin import *
from relations.DataGrid3 import *

from changeAdminBySelf import *

class QMain(QMainWindow, Ui_MainWindow):
    def __init__(self, name):    
        super(QMain, self).__init__()
        self.setupUi(self)
        
        screen=QDesktopWidget().screenGeometry()
        self.resize(screen.width(),  screen.height())
        
        self.name=name
        self.label_5.setText(self.name)
        self.pushButton.clicked.connect(self.changeself)
        self.pushButton_2.clicked.connect(self.msg)
        
        self.timer=QTimer(self)
        self.showTime()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        
        self.treeWidget.clicked.connect(self.onTreeClicked)
        self.menu_item=None
        self.admin_1=Admin_1()
        self.admin_2=Admin_2()
        self.addadmin=addadmin()
        self.addbike0=addbike()
        self.addusers=adduser()
        self.user_1=User_1()
        self.user_2=User_2()
        
        self.bike=Bike()

        self.order_1=Order_1()
        self.addorder=addOrder()

        self.changeadminbyself=changeAdminBySelf(self.name)
        
    def showTime(self): 
		# 获取系统现在的时间
        time = QDateTime.currentDateTime() 
        # 设置系统时间显示格式
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd");
        # 在标签上显示时间
        self.label_3.setText( timeDisplay )
        
    def msg(self): 
        reply=QMessageBox.information(self,  "提示信息",  "是否确认退出系统",  QMessageBox.Yes|QMessageBox.No,  QMessageBox.Yes)
        if(reply==16384):
            self.close()
        print(reply)
        
    def changeself(self): 
        self.changeadminbyself.show()
  
        
        
    def onTreeClicked(self,  qmodelindex):
        item=self.treeWidget.currentItem()
        print(item.text(0))   
       
        if(item.text(0)=="按管理员号查询"):
            print(self.menu_item)
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.admin_1
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()
        if(item.text(0)=="按管理员名查询"):
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.admin_2
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()
        if(item.text(0)=="增加管理员"):
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.addadmin
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()
            
        if(item.text(0)=="管理员信息管理"):
            print(self.menu_item)
            if self.menu_item!=None:
                self.menu_item.close()
                
            self.datagrid3=DataGrid3()
            self.menu_item=self.datagrid3
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()            
        

        if(item.text(0)=="按单车号查询"):
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.bike
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()             

        if(item.text(0)=="单车信息管理"):
            if self.menu_item!=None:
                self.menu_item.close()
                
            self.bikedatagrid=DataGridBike()
            self.menu_item=self.bikedatagrid
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()     
     
        if(item.text(0)=="增加单车"):
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.addbike0
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()
    
        if(item.text(0)=="增加用户"):
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.addusers
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()
        
        if(item.text(0)=="用户信息按号查询"):
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.user_1
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()       
      
        if(item.text(0)=="用户信息按名查询"):
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.user_2
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()    
      
        if(item.text(0)=="用户信息管理"):
            if self.menu_item!=None:
                self.menu_item.close()
                
            self.datagriduser3=DataGridUser3()
            self.menu_item=self.datagriduser3
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()      
            
            
        ######################################
        if(item.text(0)=="按订单号查询"):
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.order_1
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()      
          
        
      
        if(item.text(0)=="增加租赁关系"):
            if self.menu_item!=None:
                self.menu_item.close()
            self.menu_item=self.addorder
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()      
            
            
        if(item.text(0)=="租赁信息管理"):
            if self.menu_item!=None:
                self.menu_item.close()
                
            self.datagridorder3=DataGridOrder3()
            self.menu_item=self.datagridorder3
            self.gridLayout.addWidget(self.menu_item)
            self.menu_item.show()             
      
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin2 = QMain("devilmaycry")  
    myWin2.show()  
    sys.exit(app.exec_())          
