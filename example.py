# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import BestEx
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 40, 481, 36))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 40, 92, 36))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClick)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 190, 751, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Documents','Smilarity'])
        self.tableWidget.setRowCount(10)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 150, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        documents = ["Human machine interface for lab abc computer applications.",
                    "A survey of user opinion of computer system response time.",
                     "The EPS user interface management system.",
              "System and human system engineering testing of EPS.",
              "Relation of user perceived response time to error measurement.",
              "The generation of random binary unordered trees.",
              "The intersection graph of paths in trees.",
              "Graph minors IV Widths of trees and well quasi ordering.",
              "Graph minors A survey."]
        for i in range(0,9):
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(documents[i]))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Similarity"))
        self.pushButton.setText(_translate("MainWindow", "Find"))
        self.label.setText(_translate("MainWindow", "Corpus"))

    def onClick(self):
        sims=BestEx.match(self.lineEdit.text())
        #self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(str(sims[0])))
        #print(sims[2])
        for i in range(0,9):
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(sims[i])))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

