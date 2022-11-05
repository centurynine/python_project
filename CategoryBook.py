# Form implementation generated from reading ui file 'uiCategoryBook.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_uiHomePage(object):
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
        self.signoutButton = QtWidgets.QPushButton(uiHomePage)
        self.signoutButton.setGeometry(QtCore.QRect(290, 600, 191, 41))
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
        self.bookAdd = QtWidgets.QPushButton(uiHomePage)
        self.bookAdd.setGeometry(QtCore.QRect(30, 70, 211, 61))
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
        self.bookEdit.setGeometry(QtCore.QRect(260, 70, 211, 61))
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

        self.retranslateUi(uiHomePage)
        QtCore.QMetaObject.connectSlotsByName(uiHomePage)

    def retranslateUi(self, uiHomePage):
        _translate = QtCore.QCoreApplication.translate
        uiHomePage.setWindowTitle(_translate("uiHomePage", "Dialog"))
        self.label.setText(_translate("uiHomePage", "สถานะหนังสือ"))
        self.signoutButton.setText(_translate("uiHomePage", "ปิดหน้าต่าง"))
        self.bookAdd.setText(_translate("uiHomePage", "เพิ่มรายการหนังสือ"))
        self.bookEdit.setText(_translate("uiHomePage", "แก้ไขรายการหนังสือ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiHomePage = QtWidgets.QDialog()
    ui = Ui_uiHomePage()
    ui.setupUi(uiHomePage)
    uiHomePage.show()
    sys.exit(app.exec())
