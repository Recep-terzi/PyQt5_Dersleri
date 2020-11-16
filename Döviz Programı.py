# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taslak8.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QVBoxLayout,QPushButton,QLabel,QLineEdit,QApplication,qApp
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(555, 544)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 430, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 450, 161, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 450, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 250, 351, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 420, 101, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 420, 161, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(200, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(70, 280, 121, 121))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 80, 111, 31))
        self.radioButton_3.setCheckable(True)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setAutoRepeat(False)
        self.radioButton_3.setAutoExclusive(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoRepeat(False)
        self.radioButton_2.setAutoExclusive(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setAutoExclusive(True)
        self.radioButton.setObjectName("radioButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 280, 131, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 80, 111, 31))
        self.radioButton_6.setCheckable(True)
        self.radioButton_6.setChecked(False)
        self.radioButton_6.setAutoRepeat(False)
        self.radioButton_6.setAutoExclusive(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.radioButton_4.setCheckable(True)
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setAutoRepeat(False)
        self.radioButton_4.setAutoExclusive(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setEnabled(True)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.radioButton_5.setCheckable(True)
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setAutoRepeat(False)
        self.radioButton_5.setAutoExclusive(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 10, 431, 231))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Hesapla"))
        self.label.setText(_translate("Form", "Sonuç"))
        self.label_2.setText(_translate("Form", "DÖNÜŞTÜRMEK İSTEDİĞİNİZ PARA BİRİMLERİNİ SEÇİNİZ"))
        self.label_3.setText(_translate("Form", "Dönüşecek Tutar"))
        self.label_4.setText(_translate("Form", "----------->"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.radioButton_3.setText(_translate("Form", "Euro"))
        self.radioButton_2.setText(_translate("Form", "Dolar"))
        self.radioButton.setText(_translate("Form", "Türk Lirası"))
        self.groupBox_2.setTitle(_translate("Form", "GroupBox"))
        self.radioButton_6.setText(_translate("Form", "Euro"))
        self.radioButton_4.setText(_translate("Form", "Dolar"))
        self.radioButton_5.setText(_translate("Form", "Türk Lirası"))

        self.pushButton.clicked.connect(self.uygulama)

    def uygulama(self):

        url = "https://kur.doviz.com"
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        oranlar = soup.find_all("span", {"class": "value"})
        basliklar = soup.find_all("span", {"class": "name"})

        liste_oranlar = []
        liste_basliklar = []

        for liste, oran in zip(oranlar, basliklar):
            liste = liste.text
            oran = oran.text
            self.textEdit.append("{} -----------> {}".format(oran, liste))

        for a in oranlar:
            liste_oranlar.append(a.text)
        for b in basliklar:
            liste_basliklar.append((b.text).replace(",", "."))



        if self.radioButton.isChecked():
            if self.radioButton_5.isChecked():

                b = self.lineEdit_2.text()

                self.islem = float(b) / float(b)

                self.lineEdit.setText(str(self.islem))

            elif self.radioButton_4.isChecked():

                pass

            elif self.radioButton_6.isChecked():
                pass
        if self.radioButton_2.isChecked():
            if self.radioButton_4.isChecked():
                pass
            elif self.radioButton_5.isChecked():
                pass
            elif self.radioButton_6.isChecked():
                pass
        if self.radioButton_3.isChecked():
            if self.radioButton_4.isChecked():
                pass
            elif self.radioButton_5.isChecked():
                pass
            elif self.radioButton_6.isChecked():
                pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

