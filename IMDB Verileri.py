import sys
from PyQt5 import QtWidgets
import os
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QWidget,QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow


class Proje(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.film_list = QtWidgets.QTextEdit()
        self.temizle = QPushButton("Temizle")
        self.listele = QPushButton("Verileri Listele")

        v_box = QVBoxLayout()
        v_box.addWidget(self.film_list)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.listele)
        v_box.addLayout(v_box)

        self.setLayout(v_box)

        self.setWindowTitle("IMDB Projesi")
        self.show()

        self.temizle.clicked.connect(self.verileri_temizle)

        self.listele.clicked.connect(self.verileri_listele)

    def verileri_temizle(self):
        self.film_list.clear()

    def verileri_listele(self):
        url = "http://www.imdb.com/chart/top"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        basliklar = soup.find_all("td", {"class": "titleColumn"})
        ratingler = soup.find_all("td", {"class", "ratingColumn imdbRating"})

        for baslik, rating in zip(basliklar, ratingler):
            baslik = baslik.text
            rating = rating.text

            baslik = baslik.strip()
            baslik = baslik.replace("\n", "")

            rating = rating.strip()
            rating = rating.replace("\n", "")

            film = ("Film ismi: {} Filmin Ratingi : {}".format(baslik, rating))
            self.film_list.append(film)


app = QApplication(sys.argv)
proje = Proje()
sys.exit(app.exec_())
