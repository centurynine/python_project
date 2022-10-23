# Form implementation generated from reading ui file 'MyApp.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 659)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.usernameText = QtWidgets.QLineEdit(Dialog)
        self.usernameText.setGeometry(QtCore.QRect(140, 180, 240, 40))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.usernameText.setFont(font)
        self.usernameText.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    backgroud-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"backgroud-color: rgb(43, 45, 56);\n"
"}")
        self.usernameText.setObjectName("usernameText")
        self.passwordText = QtWidgets.QLineEdit(Dialog)
        self.passwordText.setGeometry(QtCore.QRect(140, 260, 240, 40))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.passwordText.setFont(font)
        self.passwordText.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    backgroud-color: rgb(27, 29, 35);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"backgroud-color: rgb(43, 45, 56);\n"
"}")
        self.passwordText.setObjectName("passwordText")
        self.loginbutton = QtWidgets.QPushButton(Dialog)
        self.loginbutton.setGeometry(QtCore.QRect(180, 370, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    backgroud-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:hover:pressed\n"
"{\n"
"  border: 2px solid rgb(255, 73, 73);\n"
"}")
        self.loginbutton.setObjectName("loginbutton")
        self.fetchdata = QtWidgets.QPushButton(Dialog)
        self.fetchdata.setGeometry(QtCore.QRect(160, 480, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.fetchdata.setFont(font)
        self.fetchdata.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    backgroud-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:hover:pressed\n"
"{\n"
"  border: 2px solid rgb(255, 73, 73);\n"
"}")
        self.fetchdata.setObjectName("fetchdata")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.usernameText.setPlaceholderText(_translate("Dialog", "Username"))
        self.passwordText.setPlaceholderText(_translate("Dialog", "Password"))
        self.loginbutton.setText(_translate("Dialog", "Login"))
        self.fetchdata.setText(_translate("Dialog", "Fetch data"))
        self.loginbutton.clicked.connect(self.callSql)
        self.fetchdata.clicked.connect(self.callDatabase)


    def callSql(self):
        username = self.usernameText.text()
        passsword = self.passwordText.text()
        con = pymysql.connect(host="localhost", database="python_project", user=username, password=passsword, charset="utf8")
        print(con)

    def callDatabase(self):
        username = self.usernameText.text()
        passsword = self.passwordText.text()
        sqlConnection = pymysql.connect(host="localhost", database="python_project", user=username, password=passsword,
         charset="utf8")
        print(sqlConnection)

        with sqlConnection:
                with sqlConnection.cursor() as cursor:
                # Create a new record
                        sql = "INSERT INTO `users` (`username`, `password`, `displayname`) VALUES (%s, %s, %s)"
                        cursor.execute(sql, ('username', 'passsword', 'displaynametest'))
                        cursor = sqlConnection.cursor()
                        cursor.close()
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        sqlConnection.commit()

        #with sqlConnection.cursor() as cursor:
        #       # Read a single record
        ##       sql = "SELECT `id`, `password` FROM `users` WHERE `username`=%s"
        #       cursor.execute(sql, (passsword,))
        #       result = cursor.fetchone()
        #      print(result)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
