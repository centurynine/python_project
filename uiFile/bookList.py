from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_uiHomePage(object):
    def setupUi(self, uiHomePage):
        uiHomePage.setObjectName("uiHomePage")
        uiHomePage.resize(495, 659)
        uiHomePage.setAutoFillBackground(False)
        uiHomePage.setStyleSheet("background-color: rgb(27, 29, 35);")
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
        self.bookDelete.setGeometry(QtCore.QRect(30, 300, 211, 61))
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
        self.bookStatus = QtWidgets.QPushButton(uiHomePage)
        self.bookStatus.setGeometry(QtCore.QRect(260, 300, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.bookStatus.setFont(font)
        self.bookStatus.setStyleSheet("QPushButton {\n"
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
        self.bookStatus.setObjectName("bookStatus")

        self.retranslateUi(uiHomePage)
        QtCore.QMetaObject.connectSlotsByName(uiHomePage)

    def retranslateUi(self, uiHomePage):
        _translate = QtCore.QCoreApplication.translate
        uiHomePage.setWindowTitle(_translate("uiHomePage", "Dialog"))
        self.label.setText(_translate("uiHomePage", "Read with me"))
        self.signoutButton.setText(_translate("uiHomePage", "??????????????????????????????"))
        self.bookList.setText(_translate("uiHomePage", "???????????????????????????????????????"))
        self.bookAdd.setText(_translate("uiHomePage", "??????????????????????????????????????????????????????"))
        self.bookEdit.setText(_translate("uiHomePage", "??????????????????????????????????????????????????????"))
        self.bookDelete.setText(_translate("uiHomePage", "?????????????????????????????????????????????"))
        self.aboutusButton.setText(_translate("uiHomePage", "About us"))
        self.bookStatus.setText(_translate("uiHomePage", "????????????????????????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiHomePage = QtWidgets.QDialog()
    ui = Ui_uiHomePage()
    ui.setupUi(uiHomePage)
    uiHomePage.show()
    sys.exit(app.exec())
