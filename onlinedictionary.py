from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import speech_recognition as sr
import pyttsx3 as pe
from googletrans import Translator
from PyDictionary import PyDictionary as p
import json


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(510, 30, 361, 321))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 10, 281, 16))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(220, 70, 281, 81))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(220, 160, 281, 91))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(220, 260, 281, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(220, 320, 281, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 80, 47, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 190, 47, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 270, 47, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 326, 47, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 10, 47, 13))
        self.label_6.setObjectName("label_6")
        self.tts = QtWidgets.QPushButton(self.centralwidget)
        self.tts.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.tts.setObjectName("tts")
        self.stt = QtWidgets.QPushButton(self.centralwidget)
        self.stt.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.stt.setObjectName("stt")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(50, 130, 75, 23))
        self.clear.setObjectName("clear")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(50, 170, 75, 23))
        self.run.setObjectName("run")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(50, 210, 75, 23))
        self.quit.setObjectName("quit")
        self.savepath = QtWidgets.QLineEdit(self.centralwidget)
        self.savepath.setGeometry(QtCore.QRect(10, 270, 151, 20))
        self.savepath.setText("")
        self.savepath.setObjectName("savepath")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 101, 16))
        self.label_7.setObjectName("label_7")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(10, 300, 75, 23))
        self.save.setObjectName("save")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 30, 31, 16))
        self.label_8.setObjectName("label_8")
        self.tts_2 = QtWidgets.QPushButton(self.centralwidget)
        self.tts_2.setGeometry(QtCore.QRect(50, 10, 75, 23))
        self.tts_2.setObjectName("tts_2")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(220, 30, 281, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear.clicked.connect(self.clearing)
        self.quit.clicked.connect(self.quiting)
        self.run.clicked.connect(self.running)
        self.save.clicked.connect(self.savejs)
        self.stt.clicked.connect(self.stf)
        self.tts.clicked.connect(self.wordps)
        self.tts_2.clicked.connect(self.meanps)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def quiting(self):
        sys.exit()
    def clearing(self):
        app.processEvents()
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.textBrowser_3.clear()
        self.textBrowser_4.clear()
        self.textBrowser_5.clear()
        self.textBrowser_6.clear()
        self.lineEdit.clear()
        self.savepath.clear()
    def stf(self):
        self.textBrowser_5.append("Speak")
        app.processEvents()
        r=sr.Recognizer()
        with sr.Microphone() as s:
            audio=r.listen(s)    
        self.textBrowser_6.append(r.recognize_google(audio))
        self.textBrowser_5.clear()
        self.textBrowser_5.append("Done!")
    def running(self):
        self.textBrowser_5.append("Starting...")
        app.processEvents()
        if self.lineEdit.text()=="":
            word=self.textBrowser_6.toPlainText()
            ts,dic=Translator(),p()
            persian=ts.translate(word,dest="fa")
            englishdic=dic.meaning(word)
            try:
                syn,ant=dic.synonym(word),dic.antonym(word)
            except:
                self.textBrowser_2.append("not found")
                self.textBrowser_3.append("not found")
            else:    
                for i in englishdic:
                    self.textBrowser.append(i+":")
                    self.textBrowser.append("\n".join(englishdic[i]))
                self.textBrowser_2.append("\n".join(syn))
                self.textBrowser_3.append("\n".join(ant))
                self.textBrowser_4.append(persian.text)
        else:
            word=self.lineEdit.text()
            ts,dic=Translator(),p()
            persian=ts.translate(word,dest="fa")
            englishdic=dic.meaning(word)
            try:    
                syn,ant=dic.synonym(word),dic.antonym(word)
            except:
                self.textBrowser_2.append("not found")
                self.textBrowser_3.append("not found")
            else: 
                for i in englishdic:
                    self.textBrowser.append(i+":")
                    self.textBrowser.append("\n".join(englishdic[i]))
                self.textBrowser_2.append("\n".join(syn))
                self.textBrowser_3.append("\n".join(ant))
                self.textBrowser_4.append(persian.text)    
        self.textBrowser_5.clear()
        self.textBrowser_5.append("Done!")
    def savejs(self):
        app.processEvents()
        if self.savepath.text()=="":
            self.textBrowser_5.append("No path entered")
        else:
            givenpath=self.savepath.text()
            if givenpath[-1] !="/":
                givenpath=givenpath+"/"
                if self.textBrowser_6.toPlainText()=="" and self.lineEdit.text()=="":
                        self.textBrowser_5.append("No word for saving")
                elif self.textBrowser_5.toPlainText()=="":
                    name=self.lineEdit.text()
                    directpath=givenpath+name+".json"
                    with open(directpath,'w') as file:
                        finalinfo={"word":self.lineEdit.text(),
                                    "meaning":self.textBrowser.toPlainText(),
                                    "synonym":self.textBrowser_2.toPlainText(),
                                    "antonym":self.textBrowser_3.toPlainText(),
                                    "persian":self.textBrowser_4.toPlainText(),
                        }
                        json.dump(finalinfo,file)
                    self.textBrowser_5.append("saved")
                elif self.lineEdit.text()=="":
                    name=self.textBrowser_6.toPlainText()
                    directpath=givenpath+name+".json"
                    with open(directpath,'w') as file:
                        finalinfo={"word":self.textBrowser_6.toPlainText(),
                                    "meaning":self.textBrowser.toPlainText(),
                                    "synonym":self.textBrowser_2.toPlainText(),
                                    "antonym":self.textBrowser_3.toPlainText(),
                                    "persian":self.textBrowser_4.toPlainText(),
                        }
                        json.dump(finalinfo,file)
                    self.textBrowser_5.append("saved")
            else:
                if self.textBrowser_6.toPlainText()=="" and self.lineEdit.text()=="":
                        self.textBrowser_5.append("No word for saving")
                elif self.textBrowser_5.toPlainText()=="":
                    name=self.lineEdit.text()
                    directpath=givenpath+name+".json"
                    with open(directpath,'w') as file:
                        finalinfo={"word":self.lineEdit.text(),
                                    "meaning":self.textBrowser.toPlainText(),
                                    "synonym":self.textBrowser_2.toPlainText(),
                                    "antonym":self.textBrowser_3.toPlainText(),
                                    "persian":self.textBrowser_4.toPlainText(),
                        }
                        json.dump(finalinfo,file)
                    self.textBrowser_5.append("saved")
                elif self.lineEdit.text()=="":
                    name=self.textBrowser_6.toPlainText()
                    directpath=givenpath+name+".json"
                    with open(directpath,'w') as file:
                        finalinfo={"word":self.textBrowser_6.toPlainText(),
                                    "meaning":self.textBrowser.toPlainText(),
                                    "synonym":self.textBrowser_2.toPlainText(),
                                    "antonym":self.textBrowser_3.toPlainText(),
                                    "persian":self.textBrowser_4.toPlainText(),
                        }
                        json.dump(finalinfo,file)
                    self.textBrowser_5.append("saved")
    def wordps(self):
        app.processEvents()
        en=pe.init()
        if self.lineEdit.text()=="":
            en.say(self.textBrowser_6.toPlainText())
            en.runAndWait()
        else:
            en.say(self.lineEdit.text())
            en.runAndWait()
    def meanps(self):
        app.processEvents()
        e=pe.init()
        e.say(self.textBrowser.toPlainText())
        e.runAndWait()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Onlinedictionary"))
        self.label.setText(_translate("MainWindow", "input word:"))
        self.label_2.setText(_translate("MainWindow", "synonym:"))
        self.label_3.setText(_translate("MainWindow", "antonym:"))
        self.label_4.setText(_translate("MainWindow", "persian:"))
        self.label_5.setText(_translate("MainWindow", "Status:"))
        self.label_6.setText(_translate("MainWindow", "meaning:"))
        self.tts.setText(_translate("MainWindow", "word prnc"))
        self.stt.setText(_translate("MainWindow", "Speak!"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.run.setText(_translate("MainWindow", "Translate"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        self.savepath.setPlaceholderText(_translate("MainWindow", "path example: C:/Users/..."))
        self.label_7.setText(_translate("MainWindow", "save as json file:"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.label_8.setText(_translate("MainWindow", "word:"))
        self.tts_2.setText(_translate("MainWindow", "meaning prnc"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

