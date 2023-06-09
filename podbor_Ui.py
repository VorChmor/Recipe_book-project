# Form implementation generated from reading ui file 'podbor.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import defs
param = sys.argv[1]
class Ui_MainWindow(object):
    def setupUi(self, MainWindow,param):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 70, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 60, 441, 491))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(520, 120, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(lambda index: self.add_dish(index,param))
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(520, 250, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.currentIndexChanged.connect(lambda index: self.vibor_dish(index))
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 30, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 520, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(lambda: defs.go_to_new_file("poisk_Ui.py"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Выберите категорию"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Первые блюда"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Вторые блюда"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Закуски"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Салаты"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Напитки"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Десерты"))
        self.label_2.setText(_translate("MainWindow", "Выберите блюдо"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))
    
    def add_dish(self,index,param):
        self.comboBox_2.clear()
        kategory= self.comboBox.itemText(index)
        fetch_dish=defs.vabor_category(kategory,param)
        for dish_name in fetch_dish:
            self.comboBox_2.addItem(dish_name[1])
    def vibor_dish(self,index):
        self.textEdit_2.clear()
        self.textEdit.clear()
        name_dish = self.comboBox_2.currentText()
        fetch_dish=defs.vivod_recipe(name_dish)
        self.textEdit_2.setText(fetch_dish[3])
        self.textEdit.setText(fetch_dish[1])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,param)
    MainWindow.show()
    sys.exit(app.exec())
