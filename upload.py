from turtle import home
from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql
from database import *

class Ui_Dialog(object):
    def setupUi(self, Upload):
        Upload.setObjectName("Dialog")
        Upload.resize(495, 659)
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(12)
        Upload.setFont(font)
        Upload.setAutoFillBackground(False)
        Upload.setStyleSheet("background-color: rgb(27, 29, 35);")
        Upload.setWindowIcon(QtGui.QIcon('icon.png'))
        self.booknameText = QtWidgets.QLineEdit(Upload)
        self.booknameText.setGeometry(QtCore.QRect(70, 100, 371, 40))
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
        self.authorText = QtWidgets.QLineEdit(Upload)
        self.authorText.setGeometry(QtCore.QRect(70, 160, 371, 41))
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
        self.addButton = QtWidgets.QPushButton(Upload)
        self.addButton.setGeometry(QtCore.QRect(100, 570, 161, 51))
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
        self.costText = QtWidgets.QLineEdit(Upload)
        self.costText.setGeometry(QtCore.QRect(70, 220, 371, 41))
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
        self.label = QtWidgets.QLabel(Upload)
        self.label.setGeometry(QtCore.QRect(30, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
                                 "    Color: #FFF\n"
                                 "}")
        self.label.setObjectName("label")
        self.cancelButton = QtWidgets.QPushButton(Upload)
        self.cancelButton.setGeometry(QtCore.QRect(290, 580, 101, 41))
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
        self.descriptionText = QtWidgets.QPlainTextEdit(Upload)
        self.descriptionText.setGeometry(QtCore.QRect(70, 280, 361, 251))
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

        self.retranslateUi(Upload)
        QtCore.QMetaObject.connectSlotsByName(Upload)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.booknameText.setPlaceholderText(
            _translate("Dialog", "ชื่อหนังสือ"))
        self.authorText.setPlaceholderText(_translate("Dialog", "ผู้แต่ง"))
        self.addButton.setText(_translate("Dialog", "เพิ่มข้อมูล"))
        self.costText.setPlaceholderText(_translate("Dialog", "ราคา"))
        self.label.setText(_translate("Dialog", "เพิ่มรายการหนังสือ"))
        self.cancelButton.setText(_translate("Dialog", "ยกเลิก"))
        self.descriptionText.setPlaceholderText(
            _translate("Dialog", "รายละเอียด"))
        self.addButton.clicked.connect(self.insertDatabase)
        self.cancelButton.clicked.connect(self.cancelAddData)

    def insertDatabase(self):
        book = self.booknameText.text()
        author = self.authorText.text()
        cost = self.costText.text()
        description = self.descriptionText.toPlainText()
        if (book == '' or author == '' or cost == '' or description == ''):
            print("Please fill all data")
        else:
            con = pymysql.connect(host="localhost", database="python_project",
                                  user=userSQL, password=passSQL, charset="utf8")
            cursor = con.cursor()
            cursor.execute("INSERT INTO books (book_name, author, cost, description) VALUES (%s, %s, %s, %s)",
                           (book, author, cost, description))
            con.commit()
            self.booknameText.setText("")
            self.authorText.setText("")
            self.costText.setText("")
            self.descriptionText.setPlainText("")

    def cancelAddData(self):
        self.booknameText.setText("")
        self.authorText.setText("")
        self.costText.setText("")
        self.descriptionText.setPlainText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
