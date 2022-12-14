# Form implementation generated from reading ui file 'uiAboutUs.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_uiAboutUs(object):
    def setupUi(self, uiHomePage):
        uiHomePage.setObjectName("uiHomePage")
        uiHomePage.resize(495, 659)
        uiHomePage.setAutoFillBackground(False)
        uiHomePage.setStyleSheet("background-color: rgb(27, 29, 35);")
        uiHomePage.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label = QtWidgets.QLabel(uiHomePage)
        self.label.setGeometry(QtCore.QRect(150, 30, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    Color: #FFF\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.closeButton = QtWidgets.QPushButton(uiHomePage)
        self.closeButton.setGeometry(QtCore.QRect(350, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(12)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton {\n"
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
        self.closeButton.setObjectName("closeButton")
        self.name1 = QtWidgets.QPushButton(uiHomePage)
        self.name1.setGeometry(QtCore.QRect(50, 120, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(14)
        self.name1.setFont(font)
        self.name1.setStyleSheet("QPushButton {\n"
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
        self.name1.setObjectName("name1")
        self.name2 = QtWidgets.QPushButton(uiHomePage)
        self.name2.setGeometry(QtCore.QRect(50, 200, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(14)
        self.name2.setFont(font)
        self.name2.setStyleSheet("QPushButton {\n"
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
        self.name2.setObjectName("name2")

        self.retranslateUi(uiHomePage)
        QtCore.QMetaObject.connectSlotsByName(uiHomePage)

    def retranslateUi(self, uiHomePage):
        _translate = QtCore.QCoreApplication.translate
        uiHomePage.setWindowTitle(_translate("uiHomePage", "About us"))
        self.label.setText(_translate("uiHomePage", "About us"))
        self.closeButton.setText(_translate("uiHomePage", "?????????????????????????????????"))
        self.name1.setText(_translate("uiHomePage", "????????????????????? ???????????????????????? 116310400136-2"))
        self.name2.setText(_translate("uiHomePage", "?????????????????????????????? ?????????????????????????????????????????? 116310400125-5"))
        self.closeButton.clicked.connect(uiHomePage.close)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uiHomePage = QtWidgets.QDialog()
    ui = Ui_uiAboutUs()
    ui.setupUi(uiHomePage)
    uiHomePage.show()
    sys.exit(app.exec())
