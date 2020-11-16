import sys
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QLineEdit,QDialog
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow
from PyQt5 import QtWidgets,QtGui

class Ui_YanEkran(QtWidgets):
    def __init__(self):
        super().__init__()

        self.title = "Ana Ekran"

        self.Pencere1()

    def Pencere1(self,YanEkran):
        self.setWindowTitle(self.title)
        self.setGeometry(500, 400, 400, 100)

        v_box = QVBoxLayout()

        self.giris = QPushButton("Giriş Yap")
        self.eposta = QLineEdit("Eposta Adresinizi Giriniz")
        self.sifre = QLineEdit("Şifrenizi giriniz")
        self.yazi = QLabel()
        v_box.addWidget(self.eposta)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.giris)
        v_box.addWidget(self.yazi)

        self.setLayout(v_box)

        self.show()

App = QApplication(sys.argv)
pencere = Pencere()

sys.exit(App.exec_())