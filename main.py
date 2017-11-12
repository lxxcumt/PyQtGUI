# encoding: utf-8
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
        self.connect(self.pushButton_8, QtCore.SIGNAL("clicked()"), self.Dia_input)
        self.connect(self.pushButton_9, QtCore.SIGNAL("clicked()"), self.input_int)
        self.connect(self.pushButton_10, QtCore.SIGNAL("clicked()"), self.input_item)
        self.connect(self.actionOpen, QtCore.SIGNAL("triggered()"), self.menu_open)
        self.connect(self.actionAbout, QtCore.SIGNAL("triggered()"), self.msg_about)
        self.connect(self.actionInformation, QtCore.SIGNAL("triggered()"), self.msg)
        self.connect(self.actionSave, QtCore.SIGNAL("triggered()"), self.menu_save)


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
        reply = QMessageBox.information(self, u"Title", u"information", QMessageBox.Yes|QMessageBox.No)
        print reply

    def msg_Ques(self):
        answer = QMessageBox.question(self, u"Question",u"Yes or No?", "OK","Cancel","I don't know either") #"OK","Cancel","I don't know either"
        print answer

    def msg_warn(self):
        warning = QMessageBox.warning(self, u"Warning", u"Virus Attack", "OK","Cancel")
        print warning

    def msg_about(self):
        mybutton = QMessageBox.about(self, u"Description", u"This is a very wonderful APP!!!!")

    def Dia_input(self):
        my_str, stat = QInputDialog.getText(self, u'Input Dialog',u'Please input string', QLineEdit.Normal, u'please input information here')
        print unicode(my_str)

    def input_int(self):
        my_int, stat_int = QInputDialog.getInteger(self, u'Int input',u'please input an int', 90, 0, 100 )
        print  my_int

    def input_item(self):
        my_list = QStringList()
        my_list.append(u'Apple')
        my_list.append(u'Banana')
        my_list.append(u'Peach')
        my_item, stat_itm = QInputDialog.getItem(self, u"Input Item", u'please select: ', my_list)
        self.textBrowser.append(my_item)
        print unicode(my_item)


    def menu_open(self):
        from win32com import client as wc
        word = wc.Dispatch('Word.Application')  # win32可以调用任意Windows Application
        word.Visible = 0
        print unicode('Open')
        filepath = QtGui.QFileDialog.getOpenFileName(self,u'open the file','/')
        print filepath
        if filepath[-4:] =='.doc' or filepath[-5:] =='.docx':

            myword_doc = word.Documents.Open(unicode(filepath).replace('/','\\')) #使用'\\'代替'/'， 文件 路径分隔符
            my_count = myword_doc.Paragraphs.Count
            for i in range(my_count):
                my_pr = myword_doc.Paragraphs[i].Range
                print unicode(my_pr.text)
            myword_doc.Close
        elif filepath[-4:] == '.txt':
            f = open(unicode(filepath))
            mydata = f.read()
            f.close()
            self.textBrowser.append(mydata.decode('gbk', 'ignore'))
        else:
            QMessageBox.information(self, u'information', u'not specified type')

    def menu_save(self):
        mydata = self.textBrowser.toPlainText()
        myfile = QtGui.QFileDialog.getSaveFileName(self, u"save as ...",'/')
        print unicode(myfile)
        f=open(unicode(myfile), 'a+')
        f.write(unicode(mydata).encode('utf8'))
        f.close()



def main():
    app=QtGui.QApplication(sys.argv)
    ui=MyWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

