# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import socket

from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
import defs
class Ui_profile(object):
    def setupUi(self, profile):
        profile.setObjectName("profile")
        profile.resize(600, 400)
        font = QtGui.QFont()
        font.setPointSize(12)
        profile.setFont(font)
        profile.setStyleSheet("background-color: rgb(218,236,255);")
        self.centralwidget = QtWidgets.QWidget(parent=profile)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 290, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(136,155,211); ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 290, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(136,155,211); ")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 290, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(136,155,211); ")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 200, 200))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 100, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 180, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        profile.setCentralWidget(self.centralwidget)

        self.pushButton_2.clicked.connect(lambda: defs.go_to_new_file("sertifikat.py"))
        self.pushButton_3.clicked.connect(lambda: defs.go_to_new_file("GL_Ui.py"))

        self.retranslateUi(profile)
        QtCore.QMetaObject.connectSlotsByName(profile)

    def retranslateUi(self, profile):
        hostname = socket.gethostname()
        conn = sqlite3.connect('Recipe_book.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM state")
        results = cursor.fetchone()
        conn.close()
        _translate = QtCore.QCoreApplication.translate
        profile.setWindowTitle(_translate("profile", "MainWindow"))
        self.pushButton.setText(_translate("profile", "Избранное"))
        self.pushButton_2.setText(_translate("profile", "Сертификат"))
        self.pushButton_3.setText(_translate("profile", "На главную"))
        self.label_2.setText(_translate("profile", f"Имя пользователя: {hostname}"))
        self.label_3.setText(_translate("profile", f"Приготовлено блюд: {results[0]}"))
        self.label_4.setText(_translate("profile", f"Ранг: {results[1]}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile = QtWidgets.QMainWindow()
    ui = Ui_profile()
    ui.setupUi(profile)
    profile.show()
    sys.exit(app.exec())