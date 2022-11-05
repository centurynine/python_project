from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql
import homepage
from database import *
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 659)
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.usernameText = QtWidgets.QLineEdit(Dialog)
        self.usernameText.setGeometry(QtCore.QRect(70, 180, 381, 51))
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
        self.registerPageButton = QtWidgets.QPushButton(Dialog)
        self.registerPageButton.setGeometry(QtCore.QRect(180, 440, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.registerPageButton.setFont(font)
        self.registerPageButton.setStyleSheet("QPushButton {\n"
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
        self.registerPageButton.setObjectName("registerPageButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    Color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(190, 360, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton {\n"
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
        self.loginButton.setObjectName("loginButton")
        self.passwordText = QtWidgets.QLineEdit(Dialog)
        self.passwordText.setGeometry(QtCore.QRect(70, 250, 381, 51))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.usernameText.setPlaceholderText(_translate("Dialog", "Username"))
        self.registerPageButton.setText(_translate("Dialog", "สมัครสมาชิก"))
        self.label.setText(_translate("Dialog", "เข้าสู่ระบบ"))
        self.loginButton.setText(_translate("Dialog", "เข้าสู่ระบบ"))
        self.passwordText.setPlaceholderText(_translate("Dialog", "Password"))
        self.loginButton.clicked.connect(self.callDatabase)
        self.registerPageButton.clicked.connect(self.callRegisterPage)


    def callDatabase(self):
        username = self.usernameText.text()
        password = self.passwordText.text()
        try:
          sqlConnection = pymysql.connect(host=host, database="python_project", user='root', password='',
                                        charset="utf8")
                                        
          with sqlConnection.cursor() as cursor:
            sql = "SELECT `id` FROM `users` WHERE username=%s"
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            print(result)
            if result is not None:
                with sqlConnection.cursor() as cursor:
                    sql = "SELECT `id` FROM `users` WHERE password=%s"
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

    def callRegisterPage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_registerPage()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.close()
       # closeWindows()


def closeWindows():
    Dialog.close()

def openHomepage2():
  #  Ui_Dialog.Dialog.hide()
    Dialog2 = QtWidgets.QDialog()
    ui = homepage.Ui_uiHomePage()
    ui.setupUi(Dialog2)
    Dialog2.show()
    Dialog2.exec()

class Ui_registerPage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(495, 659)
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.usernameText = QtWidgets.QLineEdit(Dialog)
        self.usernameText.setGeometry(QtCore.QRect(70, 150, 381, 51))
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
        self.registerButton = QtWidgets.QPushButton(Dialog)
        self.registerButton.setGeometry(QtCore.QRect(180, 460, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(18)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton {\n"
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
        self.registerButton.setObjectName("registerButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 30, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    Color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.label.setObjectName("label")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(370, 600, 101, 41))
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
        self.passwordText = QtWidgets.QLineEdit(Dialog)
        self.passwordText.setGeometry(QtCore.QRect(70, 250, 381, 51))
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
        self.confirmPasswordText = QtWidgets.QLineEdit(Dialog)
        self.confirmPasswordText.setGeometry(QtCore.QRect(70, 320, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Cloud Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.confirmPasswordText.setFont(font)
        self.confirmPasswordText.setStyleSheet("QLineEdit {\n"
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
        self.confirmPasswordText.setObjectName("confirmPasswordText")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.usernameText.setPlaceholderText(_translate("Dialog", "Username"))
        self.registerButton.setText(_translate("Dialog", "สมัครสมาชิก"))
        self.label.setText(_translate("Dialog", "สมัครสมาชิก"))
        self.cancelButton.setText(_translate("Dialog", "ยกเลิก"))
        self.passwordText.setPlaceholderText(_translate("Dialog", "Password"))
        self.confirmPasswordText.setPlaceholderText(_translate("Dialog", "Confirm Password"))
        self.registerButton.clicked.connect(self.register)

    def register(self):
        username = self.usernameText.text()
        password = self.passwordText.text()
        confirmPassword = self.confirmPasswordText.text()
        if username == "" or password == "" or confirmPassword == "":
            print("กรุณากรอกข้อมูลให้ครบ")
        elif password != confirmPassword:
            print("รหัสผ่านไม่ตรงกัน")
        else:
                try:
                        sqlConnection = pymysql.connect(host=host, database=database, user=userSQL, password=passSQL,
                                                        charset="utf8")  
                        with sqlConnection.cursor() as cursor:
                                sql = "SELECT `id` FROM `users` WHERE username=%s"
                                cursor.execute(sql, (username))
                                result = cursor.fetchone()
                                print(result)
                                if result is None:
                                                        sqlConnection = pymysql.connect(host=host, database=database, user=userSQL, password=passSQL,
                                                                                        charset="utf8") 
                                                        with sqlConnection.cursor() as cursor:
                                                                sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
                                                                cursor.execute(sql, (username,password))
                                                                sqlConnection.commit()
                                                                print("สมัครสมาชิกสำเร็จ")
                                                                self.openHomepage()
                                else:
                                        print("มีชื่อผู้ใช้นี้แล้ว")

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
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
