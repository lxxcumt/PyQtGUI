# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1193, 661)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 90, 311, 321))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1070, 600, 93, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(350, 440, 131, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(0, 80, 115, 19))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(0, 40, 131, 19))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(100, 430, 201, 191))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 161, 151))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.dial = QtGui.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(450, 170, 71, 91))
        self.dial.setProperty("value", 0)
        self.dial.setSliderPosition(0)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(410, 90, 151, 51))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(610, 210, 160, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(610, 90, 161, 51))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 400, 93, 28))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 450, 93, 28))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(680, 500, 93, 28))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(680, 550, 93, 28))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textBrowser.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber_2.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MyFirstUI", None))
        self.pushButton.setText(_translate("MainWindow", "Add", None))
        self.pushButton_2.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_3.setText(_translate("MainWindow", "Close", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.radioButton_5.setText(_translate("MainWindow", "KFC", None))
        self.radioButton_4.setText(_translate("MainWindow", "Chinese Food", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox", None))
        self.radioButton_3.setText(_translate("MainWindow", "I don\'t know", None))
        self.radioButton.setText(_translate("MainWindow", "Agree", None))
        self.radioButton_2.setText(_translate("MainWindow", "Disagree", None))
        self.pushButton_4.setText(_translate("MainWindow", "通知对话框", None))
        self.pushButton_5.setText(_translate("MainWindow", "询问对话框", None))
        self.pushButton_6.setText(_translate("MainWindow", "警告对话框", None))
        self.pushButton_7.setText(_translate("MainWindow", "关于对话框", None))

