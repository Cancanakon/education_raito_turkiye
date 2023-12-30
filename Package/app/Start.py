import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import  sqlite3
from designMap import Ui_ME
from designInfo import Ui_Info
from info import  infoPage


baglan  = sqlite3.connect("veri.db")

if baglan:
    print("Veri bağlandı!")
else:
    print("Veri bağlanmadı!")


class strt(QMainWindow):

    dataSend = pyqtSignal(str,str,str,str,str)

    def __init__(self,parent=None):
        super().__init__(parent)

        # QWidget.__init__(self)
        self.ui =Ui_ME()
        self.ui.setupUi(self)

        QMessageBox.about(self, "Merhaba",
                          "<font size=5>Bu programda kullanılan tüm veriler <b>TUIK kurumundan talep edilen bilgiler ile</b> hazırlanmıştır."
                          
                          "<br><br>"
                          "Daha fazla bilgi için: <a href= \"www.tuik.gov.tr\">TUIK resmi sitesine ulaşabilirsiniz.</a> "
                          "</font>"
                          )

        self.ui.btn_Getir.clicked.connect(self.araClicked)
        self.ui.btn_HaritadaGoster.clicked.connect(self.haritadaClicked)
        TownId= 1
        sui = self.ui
        if sui.lbl_Ankara.clicked==True:
            TownId=6



        selectedTown= str(TownId)


        veri = baglan.cursor()
        getir = veri.execute('SELECT * FROM data WHERE il_id=' + selectedTown + '')
        gelen = getir.fetchall()
        print(gelen)

        baglan.commit()

        for i in gelen:
            print(i)
        print(i[1])
        sehirAdClick = str(i[1])
        OkurYazarSayClick = str(i[2])
        OkurYazarOlmSayClick = str(i[3])
        OkurYazarYuzdeClick = str(i[4])
        NufusClick= str(i[5])

        self.ui.lbl_MainSehir.setText(sehirAdClick)
        self.ui.lbl_Mainokuryazar.setText(OkurYazarSayClick)
        self.ui.lbl_Mainokuryazarolmayan.setText(OkurYazarOlmSayClick)
        self.ui.lbl_Mainokuryazaroran.setText(OkurYazarYuzdeClick)
        self.ui.lbl_Mainnufus.setText(NufusClick)



    def haritadaClicked(self):
        cameCity = self.ui.cbox_sehir.currentIndex()
        nameCity = self.ui.cbox_sehir.currentText()
        selectedCity = str(cameCity + 1)
        print(f"Şehir Numarası: {selectedCity}")

        veri = baglan.cursor()
        getir = veri.execute('SELECT * FROM data WHERE il_id=' + selectedCity + '')
        gelen = getir.fetchall()
        print(gelen)

        cameCity = int(selectedCity)
        baglan.commit()

        for i in gelen:
            print(i)
        print(i[1])
        sehirAd = str(i[1])
        OkurYazarSay = str(i[2])
        OkurYazarOlmSay = str(i[3])
        OkurYazarYuzde = str(i[4])
        Nufus = str(i[5])

        self.ui.lbl_MainSehir.setText(sehirAd)
        self.ui.lbl_Mainokuryazar.setText(OkurYazarSay)
        self.ui.lbl_Mainokuryazarolmayan.setText(OkurYazarOlmSay)
        self.ui.lbl_Mainokuryazaroran.setText(f"% {OkurYazarYuzde}")
        self.ui.lbl_Mainnufus.setText(Nufus)
        forPb = int(OkurYazarYuzde[0:2])
        self.ui.pbYuzde.setValue(forPb)


    def araClicked(self):
        self.info_object =infoPage()

        cameCity =self.ui.cbox_sehir.currentIndex()
        nameCity = self.ui.cbox_sehir.currentText()
        selectedCity = str(cameCity + 1)
        print(f"Şehir Numarası: {selectedCity}")

        veri = baglan.cursor()
        getir = veri.execute('SELECT * FROM data WHERE il_id=' + selectedCity + '')
        gelen = getir.fetchall()
        print(gelen)

        cameCity = int(selectedCity)
        baglan.commit()

        for i in gelen:
            print(i)
        print(i[1])
        sehirAd = str(i[1])
        OkurYazarSay = str(i[2])
        OkurYazarOlmSay = str(i[3])
        OkurYazarYuzde = str(i[4])
        Nufus= str(i[5])

        self.info_object.ui.lbl_sehir.setText(sehirAd)
        self.info_object.ui.lbl_okuryazar.setText(OkurYazarSay)
        self.info_object.ui.lbl_okuryazarolmayan.setText(OkurYazarOlmSay)
        self.info_object.ui.lbl_okuryazaroran.setText(f"% {OkurYazarYuzde}")
        self.info_object.ui.lbl_nufus.setText(Nufus)
        self.info_object.show()






