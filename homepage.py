from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
import book
import editdb
import upload
import pymysql
import removedb
import AboutUs
from database import *

class Ui_uiHomePage(object):
    def setupUi(self, uiHomePage):
        uiHomePage.setObjectName("uiHomePage")
        uiHomePage.resize(495, 659)
        uiHomePage.setAutoFillBackground(False)
        uiHomePage.setStyleSheet("background-color: rgb(27, 29, 35);")
        uiHomePage.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label = QtWidgets.QLabel(uiHomePage)
        self.label.setGeometry(QtCore.QRect(150, 30, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    Color: #FFF\n"
"}")
        self.label.setObjectName("label")
        self.signoutButton = QtWidgets.QPushButton(uiHomePage)
        self.signoutButton.setGeometry(QtCore.QRect(320, 600, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(12)
        self.signoutButton.setFont(font)
        self.signoutButton.setStyleSheet("QPushButton {\n"
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
        self.signoutButton.setObjectName("signoutButton")
        self.listWidget = QtWidgets.QListWidget(uiHomePage)
        self.listWidget.setGeometry(QtCore.QRect(40, 380, 421, 201))
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
        self.bookList = QtWidgets.QPushButton(uiHomePage)
        self.bookList.setGeometry(QtCore.QRect(160, 130, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.bookList.setFont(font)
        self.bookList.setStyleSheet("QPushButton {\n"
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
        self.bookList.setObjectName("bookList")
        self.bookAdd = QtWidgets.QPushButton(uiHomePage)
        self.bookAdd.setGeometry(QtCore.QRect(30, 220, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.bookAdd.setFont(font)
        self.bookAdd.setStyleSheet("QPushButton {\n"
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
        self.bookAdd.setObjectName("bookAdd")
        self.bookEdit = QtWidgets.QPushButton(uiHomePage)
        self.bookEdit.setGeometry(QtCore.QRect(260, 220, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.bookEdit.setFont(font)
        self.bookEdit.setStyleSheet("QPushButton {\n"
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
        self.bookEdit.setObjectName("bookEdit")
        self.bookDelete = QtWidgets.QPushButton(uiHomePage)
        self.bookDelete.setGeometry(QtCore.QRect(150, 300, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.bookDelete.setFont(font)
        self.bookDelete.setStyleSheet("QPushButton {\n"
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
        self.bookDelete.setObjectName("bookDelete")
        self.aboutusButton = QtWidgets.QPushButton(uiHomePage)
        self.aboutusButton.setGeometry(QtCore.QRect(20, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(12)
        self.aboutusButton.setFont(font)
        self.aboutusButton.setStyleSheet("QPushButton {\n"
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
        self.aboutusButton.setObjectName("aboutusButton")

        self.retranslateUi(uiHomePage)
        QtCore.QMetaObject.connectSlotsByName(uiHomePage)

    def retranslateUi(self, uiHomePage):
        self.addList()
        _translate = QtCore.QCoreApplication.translate
        uiHomePage.setWindowTitle(_translate("uiHomePage", "Home"))
        self.label.setText(_translate("uiHomePage", "Read with me"))
        self.signoutButton.setText(_translate("uiHomePage", "ออกจากโปรแกรม"))
        self.bookList.setText(_translate("uiHomePage", "รายการหนังสือ"))
        self.bookAdd.setText(_translate("uiHomePage", "เพิ่มรายการหนังสือ"))
        self.bookEdit.setText(_translate("uiHomePage", "แก้ไขรายการหนังสือ"))
        self.bookDelete.setText(_translate("uiHomePage", "ลบรายการหนังสือ"))
        self.aboutusButton.setText(_translate("uiHomePage", "About us"))
        self.bookList.clicked.connect(self.openBookList)
        self.bookEdit.clicked.connect(self.openEditBook)
        self.bookAdd.clicked.connect(self.openAddBook)
        self.signoutButton.clicked.connect(self.callMessageBox)
        self.bookDelete.clicked.connect(self.openRemoveBook)
        self.aboutusButton.clicked.connect(self.openAboutUs)
      #  self.signoutButton.clicked.connect(closeWindowsx)

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

    def findSel(self, current):
        currentItem = self.itemWidget(current)
        pixmap = currentItem.pixmap()
        print (pixmap)

    def openBookList(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = book.bookMain()
        self.ui.setupUi(self.window)
        self.window.show()
      #  uiHomePage.close()

    def openEditBook(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = editdb.Ui_editBook()
        self.ui.setupUi(self.window)
        self.window.show()
     #   uiHomePage.close()

    def openAddBook(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = upload.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
       # uiHomePage.close()

    def openRemoveBook(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = removedb.Ui_removeBook()
        self.ui.setupUi(self.window)
        self.window.show()
       # uiHomePage.close()

    def openAboutUs(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AboutUs.Ui_uiAboutUs()
        self.ui.setupUi(self.window)
        self.window.show()
       # uiHomePage.close()

    def signout(self):
        import sys
        sys.exit(1)


    def callMessageBox(self):
        self.messageBox('โปรดยืนยัน','ต้องการปิดโปรแกรมหรือไม่')

    def messageBox(self,title,message):
        print('messageBox')
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox().Icon.Question)
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | 
                     QMessageBox.StandardButton.No)
        x = msg.exec()
        if x == QMessageBox.StandardButton.Yes:
                import sys
                sys.exit(1)
        elif x == QMessageBox.StandardButton.No:
                print("NO!")

#     Dialog2 = QtWidgets.QDialog()
#     ui = loginpage.Ui_Dialog()
#     ui.setupUi(Dialog2)
#     Dialog2.show()
#     Dialog2.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiHomePage = QtWidgets.QDialog()
    ui = Ui_uiHomePage()
    ui.setupUi(uiHomePage)
    uiHomePage.show()
    sys.exit(app.exec())
