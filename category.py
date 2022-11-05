from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql
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
        uiHomePage.setWindowTitle(_translate("uiHomePage", "Book Status"))
        self.label.setText(_translate("uiHomePage", "สถานะหนังสือ"))
        self.exitButton.setText(_translate("uiHomePage", "ปิดหน้าต่าง"))
        self.readyButton.setText(_translate("uiHomePage", "พร้อมขาย"))
        self.emptyButton.setText(_translate("uiHomePage", "หมด"))
        self.readyButton.clicked.connect(self.readyForSale)
        self.emptyButton.clicked.connect(self.outOfStock)
        self.exitButton.clicked.connect(uiHomePage.close)
        self.listWidget.itemClicked.connect(itemActivated_event)
        self.listWidget.itemActivated.connect(self.openEditData)
        
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

    def openEditData(self):
        global selectedBook
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_editBook()
        self.ui.setupUi(self.window)
        self.window.show()
       
def itemActivated_event(item):
        itemID = item.data(1)
        print("ID : "+str(itemID))
        global selectedBook
        selectedBook = itemID


class Ui_editBook(object):
    def setupUi(self, editBook):
        editBook.setObjectName("editBook")
        editBook.resize(495, 659)
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(12)
        editBook.setFont(font)
        editBook.setAutoFillBackground(False)
        editBook.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.booknameText = QtWidgets.QLineEdit(editBook)
        self.booknameText.setGeometry(QtCore.QRect(60, 170, 371, 40))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.booknameText.setFont(font)
        self.booknameText.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.booknameText.setObjectName("booknameText")
        self.authorText = QtWidgets.QLineEdit(editBook)
        self.authorText.setGeometry(QtCore.QRect(60, 220, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.authorText.setFont(font)
        self.authorText.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.authorText.setObjectName("authorText")
        self.addButton = QtWidgets.QPushButton(editBook)
        self.addButton.setGeometry(QtCore.QRect(90, 590, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("QPushButton {\n"
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
        self.addButton.setObjectName("addButton")
        self.costText = QtWidgets.QLineEdit(editBook)
        self.costText.setGeometry(QtCore.QRect(60, 270, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.costText.setFont(font)
        self.costText.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.costText.setObjectName("costText")
        self.label = QtWidgets.QLabel(editBook)
        self.label.setGeometry(QtCore.QRect(30, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    Color: #FFF\n"
"}")
        self.label.setObjectName("label")
        self.cancelButton = QtWidgets.QPushButton(editBook)
        self.cancelButton.setGeometry(QtCore.QRect(290, 600, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton {\n"
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
        self.cancelButton.setObjectName("cancelButton")
        self.descriptionText = QtWidgets.QPlainTextEdit(editBook)
        self.descriptionText.setGeometry(QtCore.QRect(60, 320, 371, 251))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(12)
        self.descriptionText.setFont(font)
        self.descriptionText.setStyleSheet("QPlainTextEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.descriptionText.setObjectName("descriptionText")
        self.book_fetch_id = QtWidgets.QLineEdit(editBook)
        self.book_fetch_id.setGeometry(QtCore.QRect(60, 110, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.book_fetch_id.setFont(font)
        self.book_fetch_id.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.book_fetch_id.setObjectName("book_fetch_id")
        self.fetchButton = QtWidgets.QPushButton(editBook)
        self.fetchButton.setGeometry(QtCore.QRect(320, 110, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.fetchButton.setFont(font)
        self.fetchButton.setStyleSheet("QPushButton {\n"
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
        self.fetchButton.setObjectName("fetchButton")
        self.statusBook = QtWidgets.QComboBox(editBook)
        self.statusBook.setGeometry(QtCore.QRect(300, 271, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(11)
        self.statusBook.setFont(font)
        self.statusBook.setAccessibleDescription("")
        self.statusBook.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QComboBox:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.statusBook.setCurrentText("")
        self.statusBook.setObjectName("statusBook")

        self.statusBook.addItem("หมด")
        self.statusBook.addItem("พร้อมขาย")

        self.retranslateUi(editBook)
        QtCore.QMetaObject.connectSlotsByName(editBook)

    def retranslateUi(self, editBook):
        self.fecthID2()
        _translate = QtCore.QCoreApplication.translate
        editBook.setWindowTitle(_translate("editBook", "Book Status"))
        self.booknameText.setPlaceholderText(_translate("editBook", "ชื่อหนังสือ"))
        self.authorText.setPlaceholderText(_translate("editBook", "ผู้แต่ง"))
        self.addButton.setText(_translate("editBook", "แก้ไขข้อมูล"))
        self.costText.setPlaceholderText(_translate("editBook", "ราคา"))
        self.label.setText(_translate("editBook", "แก้ไขรายการหนังสือ"))
        self.cancelButton.setText(_translate("editBook", "ยกเลิก"))
        self.descriptionText.setPlaceholderText(_translate("editBook", "รายละเอียด"))
        self.book_fetch_id.setPlaceholderText(_translate("editBook", "ไอดีหนังสือ"))
        self.fetchButton.setText(_translate("editBook", "Fetch"))
        self.addButton.clicked.connect(self.editDatabase)
        self.cancelButton.clicked.connect(self.removeText)
        self.fetchButton.clicked.connect(self.fecthID)


    def fecthID2(self):
        global selectedBook
        print(selectedBook)
        global book_id
        book_id = selectedBook
        self.book_fetch_id.setText(str(book_id))
   #     print(book_id)
        # book_id = str(selectedBook)
        if selectedBook == "":
            print("กรุณาใส่ไอดีหนังสือ")
        else:
            self.checkID()

    def fecthID(self):
        global book_id
        book_id = self.book_fetch_id.text()
        if book_id == "":
            print("กรุณาใส่ไอดีหนังสือ")
        else:
            self.checkID()

    def checkID(self):
        global book_id
        con = pymysql.connect(host=host, database="python_project",
                              user=userSQL, password=passSQL, charset="utf8")
        cursor = con.cursor()
        cursor.execute("SELECT book_name FROM books WHERE book_id = %s", book_id)
        book_name = cursor.fetchone()
        if book_name == None:
            self.booknameText.setText("ไม่พบหนังสือ")
            self.authorText.setText("ไม่พบหนังสือ")
            self.costText.setText("ไม่พบหนังสือ")
            self.descriptionText.setPlainText("ไม่พบหนังสือ")
            print("ไม่พบไอดีหนังสือ")
        else:
            self.fetchDatabase()

    def fetchDatabase(self):  # ดึงข้อมูลจากฐานข้อมูลใส่ลงในช่อง Text
        print('fetching database')
        con = pymysql.connect(host="localhost", database="python_project",
                              user=userSQL, password=passSQL, charset="utf8")
        cursor = con.cursor()
        cursor.execute("SELECT book_name FROM books WHERE book_id = %s", book_id)
        book_name = cursor.fetchone()
        cursor.execute("SELECT author FROM books WHERE book_id = %s", book_id)
        author = cursor.fetchone()
        cursor.execute("SELECT cost FROM books WHERE book_id = %s", book_id)
        cost = cursor.fetchone()
        cursor.execute(
            "SELECT description FROM books WHERE book_id = %s", book_id)
        description = cursor.fetchone()
        cursor.execute("SELECT status FROM books WHERE book_id = %s", book_id)
        status = cursor.fetchone()
        self.booknameText.setText(book_name[0])
        self.authorText.setText(author[0])
        self.costText.setText(str(cost[0]))
        self.descriptionText.setPlainText(description[0])
        self.statusBook.setCurrentText(status[0])
        con.close()

    def editDatabase(self):  # แก้ไขข้อมูลในฐานข้อมูลหลังจากกดปุ่มแก้ไข
        book = self.booknameText.text()
        author = self.authorText.text()
        cost = self.costText.text()
        description = self.descriptionText.toPlainText()
        status = self.statusBook.currentText()
        if (book == '' or author == '' or cost == '' or description == '' or status == ''):
            print("Please fill all data")
        else:
            con = pymysql.connect(host="localhost", database="python_project",
                                  user=userSQL, password=passSQL, charset="utf8")
            cursor = con.cursor()
            cursor.execute("UPDATE books SET book_name=%s, author=%s, cost=%s, description=%s, status=%s WHERE book_id=%s",(book, author, cost, description, status, book_id))
            print("Edit data successfully")
            con.commit()
            con.close()


    def removeText(self):  # ล้างข้อมูลในช่อง Text
        self.booknameText.setText("")
        self.authorText.setText("")
        self.costText.setText("")
        self.descriptionText.setPlainText("")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiHomePage = QtWidgets.QDialog()
    ui = Ui_category()
    ui.setupUi(uiHomePage)
    uiHomePage.show()
    sys.exit(app.exec())
