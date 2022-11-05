from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql
from book import Ui_editBook
from database import *

class Ui_category(object):
    def setupUi(self, uiHomePage):
        uiHomePage.setObjectName("uiHomePage")
        uiHomePage.resize(495, 659)
        uiHomePage.setAutoFillBackground(False)
        uiHomePage.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.label = QtWidgets.QLabel(uiHomePage)
        self.label.setGeometry(QtCore.QRect(150, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.label.setObjectName("label")
        self.exitButton = QtWidgets.QPushButton(uiHomePage)
        self.exitButton.setGeometry(QtCore.QRect(290, 600, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(12)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:hover:pressed\n"
"{\n"
"  border: 2px solid rgb(255, 73, 73);\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.listWidget = QtWidgets.QListWidget(uiHomePage)
        self.listWidget.setGeometry(QtCore.QRect(40, 150, 421, 431))
        self.listWidget.setStyleSheet("QListWidget {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QListWidget:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QListWidget:hover:pressed\n"
"{\n"
"  border: 2px solid rgb(255, 73, 73);\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.readyButton = QtWidgets.QPushButton(uiHomePage)
        self.readyButton.setGeometry(QtCore.QRect(30, 70, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.readyButton.setFont(font)
        self.readyButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:hover:pressed\n"
"{\n"
"  border: 2px solid rgb(255, 73, 73);\n"
"}")
        self.readyButton.setObjectName("readyButton")
        self.emptyButton = QtWidgets.QPushButton(uiHomePage)
        self.emptyButton.setGeometry(QtCore.QRect(260, 70, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.emptyButton.setFont(font)
        self.emptyButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:hover:pressed\n"
"{\n"
"  border: 2px solid rgb(255, 73, 73);\n"
"}")
        self.emptyButton.setObjectName("emptyButton")

        self.retranslateUi(uiHomePage)
        QtCore.QMetaObject.connectSlotsByName(uiHomePage)

    def retranslateUi(self, uiHomePage):
        self.addList()
        _translate = QtCore.QCoreApplication.translate
        uiHomePage.setWindowTitle(_translate("uiHomePage", "Dialog"))
        self.label.setText(_translate("uiHomePage", "สถานะหนังสือ"))
        self.exitButton.setText(_translate("uiHomePage", "ปิดหน้าต่าง"))
        self.readyButton.setText(_translate("uiHomePage", "พร้อมขาย"))
        self.emptyButton.setText(_translate("uiHomePage", "หมด"))
        self.readyButton.clicked.connect(self.readyForSale)
        self.emptyButton.clicked.connect(self.outOfStock)
        self.exitButton.clicked.connect(uiHomePage.close)
        # self.listWidget.itemClicked.connect(itemActivated_event)
        # self.listWidget.itemActivated.connect(self.openEditData)

        
    def addList(self):
        print('fetching data')
        con = pymysql.connect(host=host, database="python_project",user=userSQL, password=passSQL, charset="utf8")
        cursor = con.cursor()
        cursor.execute("SELECT book_name,cost,author,book_id ,status FROM books")
        data = cursor.fetchall()
        print(data)
        for i in data:
                self.listWidget.addItem(i[0]+ "\n ราคา "+str(i[1])+" บาท\n" + " ผู้แต่ง "+str(i[2])+"\n" + " รหัสหนังสือ "+str(i[3])+"\n"+ " สถานะ "+str(i[4])+"\n")
                self.listWidget.item(data.index(i)).setData(1,i[3])
        con.close()

    def readyForSale(self):
        self.listWidget.clear()
        print('fetching data')
        con = pymysql.connect(host=host, database="python_project",user=userSQL, password=passSQL, charset="utf8")
        cursor = con.cursor()
        cursor.execute("SELECT book_name,cost,author,book_id ,status FROM books WHERE status = 'พร้อมขาย'")
        data = cursor.fetchall()
        print(data)
        for i in data:
                self.listWidget.addItem(i[0]+ "\n ราคา "+str(i[1])+" บาท\n" + " ผู้แต่ง "+str(i[2])+"\n" + " รหัสหนังสือ "+str(i[3])+"\n"+ " สถานะ "+str(i[4])+"\n")
                self.listWidget.item(data.index(i)).setData(1,i[3])
        con.close()

    def outOfStock(self):
        self.listWidget.clear()
        print('fetching data')
        con = pymysql.connect(host=host, database="python_project",user=userSQL, password=passSQL, charset="utf8")
        cursor = con.cursor()
        cursor.execute("SELECT book_name,cost,author,book_id ,status FROM books WHERE status = 'หมด'")
        data = cursor.fetchall()
        print(data)
        for i in data:
                self.listWidget.addItem(i[0]+ "\n ราคา "+str(i[1])+" บาท\n" + " ผู้แต่ง "+str(i[2])+"\n" + " รหัสหนังสือ "+str(i[3])+"\n"+ " สถานะ "+str(i[4])+"\n")
                self.listWidget.item(data.index(i)).setData(1,i[3])
        con.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiHomePage = QtWidgets.QDialog()
    ui = Ui_category()
    ui.setupUi(uiHomePage)
    uiHomePage.show()
    sys.exit(app.exec())
