# Form implementation generated from reading ui file 'redact_rezept.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import defs

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setStyleSheet("background-color: rgb(218,236,255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 971, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(246,250,255);")
        self.listWidget.setObjectName("listWidget")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(246,250,255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 350, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(580, 350, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(200, 280, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background-color: rgb(246,250,255);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(890, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_3.setFont(font)
        self.listWidget_3.setStyleSheet("background-color: rgb(246,250,255);")
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_4 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(10, 390, 531, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_4.setFont(font)
        self.listWidget_4.setStyleSheet("background-color: rgb(246,250,255);")
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_5 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(580, 390, 401, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_5.setFont(font)
        self.listWidget_5.setStyleSheet("background-color: rgb(246,250,255);")
        self.listWidget_5.setObjectName("listWidget_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 670, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(136,155,211); ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 730, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(136,155,211); ")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(lambda: defs.go_to_new_file("redactirovanie.py"))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Первые блюда"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Вторые блюда"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Закуски"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Салаты"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Напитки"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Десерты"))
        self.label.setText(_translate("MainWindow", "Выберите категорию"))
        self.label_2.setText(_translate("MainWindow", "Введите название"))
        self.label_3.setText(_translate("MainWindow", "Введите уровень"))
        self.label_4.setText(_translate("MainWindow", "Введите описание"))
        self.label_5.setText(_translate("MainWindow", "Введите продукты"))
        self.pushButton.setText(_translate("MainWindow", "Внести изменения"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
    def add_dish(self,index):
        self.listWidget.clear()
        kategory= self.comboBox.itemText(index)
        fetch_dish=defs.vabor_category_delete_dish(kategory)
        for dish_name in fetch_dish:
            self.listWidget.addItem(dish_name[1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())