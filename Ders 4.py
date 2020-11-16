import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    okay = QtWidgets.QPushButton("Tamam")#Butonlara isim vermek için kullanılır.

    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()


    h_box.addWidget(okay)#Butonları eklemeye yarar.
    h_box.addWidget(cancel)
    h_box.addStretch() #Yön Belirtmek için kullanılır.


    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 4")# Pencereye isim vermeye yarar.
    pencere.setLayout(h_box)
    pencere.setGeometry(100,100,500,500)# Pencere boyutunu ayarlamaya yarar.

    pencere.show()

    sys.exit(app.exec_())

Pencere()


