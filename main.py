from PyQt4 import QtCore, QtGui
from label import Ui_MainWindow
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

def main():
    app=QtGui.QApplication(sys.argv)
    ui=MyWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

