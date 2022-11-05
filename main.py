from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql
import homepage
from database import *
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 659)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(27, 29, 35);")
        Dialog.setWindowIcon(QtGui.QIcon('icon.png'))
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
                                        "}\n"
                                        "QLineEdit:hover {\n"
                                        "    border: 2px solid rgb(48, 50, 62);\n"
                                        "}\n"
                                        "QLineEdit:focus {\n"
                                        "    border: 2px solid rgb(85, 170, 255);\n"
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
                                        "}\n"
                                        "QLineEdit:hover {\n"
                                        "    border: 2px solid rgb(48, 50, 62);\n"
                                        "}\n"
                                        "QLineEdit:focus {\n"
                                        "    border: 2px solid rgb(85, 170, 255);\n"
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
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    border: 2px solid rgb(48, 50, 62);\n"
                                       "}\n"
                                       "QPushButton:hover:pressed\n"
                                       "{\n"
                                       "  border: 2px solid rgb(255, 73, 73);\n"
                                       "}")
        self.loginbutton.setObjectName("loginbutton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 50, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
                                 "    Color: #FFF\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Login", "Login"))
        self.usernameText.setPlaceholderText(_translate("Login", "Username"))
        self.passwordText.setPlaceholderText(_translate("Login", "Password"))
        self.loginbutton.setText(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "เข้าสู่ระบบ"))
        self.loginbutton.clicked.connect(self.callDatabase)

    def callDatabase(self):
        username = self.usernameText.text()
        password = self.passwordText.text()
        try:
          sqlConnection = pymysql.connect(host=host, database="python_project", user='root', password='',
                                        charset="utf8")
                                        
          with sqlConnection.cursor() as cursor:
            sql = "SELECT `id`, `displayname` FROM `users` WHERE username=%s"
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            print(result)
            if result is not None:
                with sqlConnection.cursor() as cursor:
                    sql = "SELECT `id`, `displayname` FROM `users` WHERE password=%s"
                    cursor.execute(sql, (password))
                    result = cursor.fetchone()
                    print(result)
                    if result is not None:
                        self.openHomepage()
            else:
                print("No data")

                
        except pymysql.err.OperationalError as e:
                print("Error %d: %s" % (e.args[0], e.args[1]))
                if(e.args[0]==1045):
                    print("Invalid username or password")
                elif(e.args[0]==1049):
                    print("Database not found")
                elif(e.args[0]==2003):
                    print("Server not found")
                elif(e.args[0]==2005):
                    print("Unknown host")
                elif(e.args[0]==2006):
                    print("Server has gone away")
                elif(e.args[0]==2013):
                    print("Lost connection to MySQL server during query")
                elif(e.args[0]==2019):
                    print("Access denied for user")
                elif(e.args[0]==2026):
                    print("Too many connections")
        else:
            print("Connection successful")
         #   self.openHomepage()
            sqlConnection.close()

    def openHomepage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = homepage.Ui_uiHomePage()
        self.ui.setupUi(self.window)
        self.window.show()
        closeWindows()

        # with sqlConnection:
        #        with sqlConnection.cursor() as cursor:
        #        # Create a new record
        #                print("Connected")

def closeWindows():
    Dialog.close()

def openHomepage2():
  #  Ui_Dialog.Dialog.hide()
    Dialog2 = QtWidgets.QDialog()
    ui = homepage.Ui_uiHomePage()
    ui.setupUi(Dialog2)
    Dialog2.show()
    Dialog2.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
