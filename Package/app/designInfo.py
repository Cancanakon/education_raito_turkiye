# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Venv_Projects/EducationMap/Package/app/infoData.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(840, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Package/app/img/info.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Info.setWindowIcon(icon)
        Info.setStyleSheet("background: rgba(74,112,139,255);color:white;border-radius: 15px;")
        self.frame_7 = QtWidgets.QFrame(Info)
        self.frame_7.setGeometry(QtCore.QRect(150, 10, 561, 131))
        self.frame_7.setStyleSheet("background:rgb(255,255,255,90);border:none;border-radius: 15px;\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.lbl_sehir = QtWidgets.QLabel(self.frame_7)
        self.lbl_sehir.setGeometry(QtCore.QRect(10, 10, 541, 111))
        self.lbl_sehir.setStyleSheet("font-size:60px;")
        self.lbl_sehir.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sehir.setObjectName("lbl_sehir")
        self.frame_8 = QtWidgets.QFrame(Info)
        self.frame_8.setGeometry(QtCore.QRect(10, 160, 821, 371))
        self.frame_8.setStyleSheet("background:rgb(255,255,255,90);border:none;border-radius: 15px;\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 281, 71))
        self.label_2.setStyleSheet("font-size:20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lbl_okuryazar = QtWidgets.QLabel(self.frame_8)
        self.lbl_okuryazar.setGeometry(QtCore.QRect(490, 20, 181, 71))
        self.lbl_okuryazar.setStyleSheet("font-size:20px;")
        self.lbl_okuryazar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_okuryazar.setObjectName("lbl_okuryazar")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        self.label_4.setGeometry(QtCore.QRect(170, 100, 281, 71))
        self.label_4.setStyleSheet("font-size:20px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setGeometry(QtCore.QRect(170, 260, 281, 71))
        self.label_5.setStyleSheet("font-size:20px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setGeometry(QtCore.QRect(170, 180, 281, 71))
        self.label_6.setStyleSheet("font-size:20px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lbl_okuryazarolmayan = QtWidgets.QLabel(self.frame_8)
        self.lbl_okuryazarolmayan.setGeometry(QtCore.QRect(490, 100, 181, 71))
        self.lbl_okuryazarolmayan.setStyleSheet("font-size:20px;")
        self.lbl_okuryazarolmayan.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_okuryazarolmayan.setObjectName("lbl_okuryazarolmayan")
        self.lbl_okuryazaroran = QtWidgets.QLabel(self.frame_8)
        self.lbl_okuryazaroran.setGeometry(QtCore.QRect(490, 180, 181, 71))
        self.lbl_okuryazaroran.setStyleSheet("font-size:20px;")
        self.lbl_okuryazaroran.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_okuryazaroran.setObjectName("lbl_okuryazaroran")
        self.lbl_nufus = QtWidgets.QLabel(self.frame_8)
        self.lbl_nufus.setGeometry(QtCore.QRect(490, 260, 181, 71))
        self.lbl_nufus.setStyleSheet("font-size:20px;")
        self.lbl_nufus.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nufus.setObjectName("lbl_nufus")

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "İşte Ayrıntılar..."))
        self.lbl_sehir.setText(_translate("Info", "ŞEHİR"))
        self.label_2.setText(_translate("Info", "OKUR-YAZAR :"))
        self.lbl_okuryazar.setText(_translate("Info", "000"))
        self.label_4.setText(_translate("Info", "OKUR-YAZAR DEĞİL:"))
        self.label_5.setText(_translate("Info", "NÜFUS:"))
        self.label_6.setText(_translate("Info", "OKUR-YAZAR ORANI:"))
        self.lbl_okuryazarolmayan.setText(_translate("Info", "000"))
        self.lbl_okuryazaroran.setText(_translate("Info", "000"))
        self.lbl_nufus.setText(_translate("Info", "000"))

