import sys
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QLineEdit,QDialog
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow
from PyQt5 import QtWidgets,QtGui,QtCore



class Mail(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Pencere"



        self.Pencere1()

    def Pencere1(self):
        self.setWindowTitle(self.title)
        self.setGeometry(500,400,400,100)

        v_box = QVBoxLayout()

        self.giris = QPushButton("Giriş Yap")
        self.eposta = QLineEdit("Eposta Adresinizi Giriniz")
        self.sifre = QLineEdit("Şifrenizi giriniz")
        self.yazi = QLabel()
        self.giris.clicked.connect(self.giris_yap)
        v_box.addWidget(self.eposta)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.giris)
        v_box.addWidget(self.yazi)

        self.setLayout(v_box)


        self.show()

    def giris_yap(self):

        self.yeni_pencere = QDialog(self)


        self.yeni_pencere.setWindowTitle("Ana Ekran")
        self.yeni_pencere.setGeometry(200,200,500,500)




        if self.eposta.text() == '123' and self.sifre.text() == '123':
            self.yazi.text() == 'Tebrikler sisteme giriş yaptınız :)'
            self.yeni_pencere.show()

        else :
            self.yazi.text() == 'Tekrar Deneyiniz'





App = QApplication(sys.argv)
mail = Mail()

sys.exit(App.exec_())



