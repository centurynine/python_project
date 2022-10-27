from re import S
from turtle import home
from PyQt6 import QtCore, QtGui, QtWidgets
from pygame import Cursor
import homepage
import pymysql
import editdb
from database import *
class bookMain(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 659)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(27, 29, 35);")
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    Color: #FFF\n"
"}")
        self.label.setObjectName("label")
        self.homeButton = QtWidgets.QPushButton(Dialog)
        self.homeButton.setGeometry(QtCore.QRect(30, 590, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("QPushButton {\n"
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
        self.homeButton.setObjectName("homeButton")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(40, 110, 421, 431))
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
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.addList()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "รายการหนังสือ"))
        self.homeButton.setText(_translate("Dialog", "ปิดหน้าต่าง"))
        self.homeButton.clicked.connect(Dialog.close)
        self.listWidget.itemClicked.connect(itemActivated_event)
        self.listWidget.itemActivated.connect(self.openEditData)

    def home(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = homepage.Ui_uiHomePage()
        self.ui.setupUi(self.window)
        self.window.show()
    #    closeWindowsz()
        
     #   QtWidgets.QDialog().hide()
    def closeWindows2(self):
        self.window = QtWidgets.QDialog()
        self.ui = bookMain()
        self.ui.setupUi(self.window)
        self.window.hide()

    def addList(self):
        print('fetching data')
        con = pymysql.connect(host="localhost", database="python_project",user=userSQL, password=passSQL, charset="utf8")
        cursor = con.cursor()
        cursor.execute("SELECT book_name,cost,author,book_id,status FROM books")
        data = cursor.fetchall()
        print(data)
        for i in data:
                self.listWidget.addItem(i[0]+ "\n ราคา "+str(i[1])+" บาท\n" + " ผู้แต่ง "+str(i[2])+"\n" + " รหัสหนังสือ "+str(i[3])+"\n"+ " สถานะ "+str(i[4])+"\n")
                self.listWidget.item(data.index(i)).setData(1,i[3])
        con.close()

    def openEditData(self):
        global selectedBook
        self.window = QtWidgets.QMainWindow()
        self.ui = editdb.Ui_editBook()
        self.ui.setupUi(self.window)
        print( "selectedBook : "+str(selectedBook) )
        self.window.show()
       
def itemActivated_event(item):
        itemID = item.data(1)
        print("ID : "+str(itemID))
        global selectedBook
        selectedBook = itemID
    
def closeWindowsz():
    Dialog.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = bookMain()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
