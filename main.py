from PyQt4 import QtCore, QtGui
from label import Ui_MainWindow
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class MyWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.ReadText)
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.ReadText)
        self.connect(self.radioButton, QtCore.SIGNAL("clicked()"), self.RadioBtn)
        self.connect(self.radioButton_4, QtCore.SIGNAL("clicked()"), self.RadioBtn_4)
        self.connect(self.dial, QtCore.SIGNAL("valueChanged(int)"), self.DialBtn)
        self.connect(self.dial, QtCore.SIGNAL("valueChanged(int)"), self.lcdNumber.display)
        self.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.msg) #self.pushButton_4.clicked.connect(self.msg)
        self.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), self.msg_Ques)
        self.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), self.msg_warn)
        self.connect(self.pushButton_7, QtCore.SIGNAL("clicked()"), self.msg_about)


    def ReadText(self):
        self.textBrowser.append(self.lineEdit.text())
    def RadioBtn(self):
        self.textBrowser.append("I agree")
        if self.radioButton.isChecked():
            print "I agree!!!!"
    def RadioBtn_4(self):
        self.textBrowser.append("I would like to eat chinese food!!!!")
        if self.radioButton_4.isChecked():
            print "I would like to eat chinese food!!!!"
    def DialBtn(self):
        self.textBrowser.append(str(self.dial.value()))
        print self.dial.value()
    def msg(self):
        reply = QMessageBox.information(self, "Title", "information", QMessageBox.Yes|QMessageBox.No)
        print reply
    def msg_Ques(self):
        answer = QMessageBox.question(self, "Question","Yes or No?", "OK","Cancel","I don't know either") #"OK","Cancel","I don't know either"
        print answer
    def msg_warn(self):
        warning = QMessageBox.warning(self, "Warning", "Virus Attack", "OK","Cancel")
        print warning
    def msg_about(self):
        description = QMessageBox.about(self, "Description", "This is a very wonderful APP!!!!")

def main():
    app=QtGui.QApplication(sys.argv)
    ui=MyWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

