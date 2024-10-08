# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui_retiradas.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_retirada(object):
    def setupUi(self, retirada):
        retirada.setObjectName("retirada")
        retirada.resize(491, 264)
        self.gridLayout_3 = QtWidgets.QGridLayout(retirada)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(retirada)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("background-color: rgb(0, 74, 153);\n"
"color: rgb(255, 255, 255);\n"
"padding: 5px 5px")
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout_3.addWidget(self.label_49, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(retirada)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 74, 153);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chk_15dias = QtWidgets.QCheckBox(retirada)
        self.chk_15dias.setStyleSheet("\n"
"            QCheckBox::indicator {\n"
"                border: 2px solid #797979;\n"
"                border-radius: 5px; /* Bordas arredondadas */\n"
"                width: 10px;\n"
"                height:10px;\n"
"            }\n"
"            QCheckBox::indicator:checked {\n"
"                background-color: #004a99; /* Cor azul quando preenchido */\n"
"            }")
        self.chk_15dias.setObjectName("chk_15dias")
        self.gridLayout_2.addWidget(self.chk_15dias, 1, 0, 1, 1)
        self.chk_5dias = QtWidgets.QCheckBox(retirada)
        self.chk_5dias.setStyleSheet("\n"
"            QCheckBox::indicator {\n"
"                border: 2px solid #797979;\n"
"                border-radius: 5px; /* Bordas arredondadas */\n"
"                width: 10px;\n"
"                height:10px;\n"
"            }\n"
"            QCheckBox::indicator:checked {\n"
"                                \n"
" background-color: #004a99; /* Cor azul quando preenchido *\n"
"            }")
        self.chk_5dias.setObjectName("chk_5dias")
        self.gridLayout_2.addWidget(self.chk_5dias, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(retirada)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 74, 153);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.ln_retirada_5 = QtWidgets.QLineEdit(retirada)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ln_retirada_5.setFont(font)
        self.ln_retirada_5.setStyleSheet("border: 2px solid #bababa; /* borda cinza */\n"
"border-radius: 5px; \n"
"padding: 2 5px;\n"
"")
        self.ln_retirada_5.setText("")
        self.ln_retirada_5.setObjectName("ln_retirada_5")
        self.gridLayout_2.addWidget(self.ln_retirada_5, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(retirada)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 74, 153);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        self.ln_retirada_15 = QtWidgets.QLineEdit(retirada)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ln_retirada_15.setFont(font)
        self.ln_retirada_15.setStyleSheet("border: 2px solid #bababa; /* borda cinza */\n"
"border-radius: 5px; \n"
"padding: 2 5px;\n"
"")
        self.ln_retirada_15.setText("")
        self.ln_retirada_15.setObjectName("ln_retirada_15")
        self.gridLayout_2.addWidget(self.ln_retirada_15, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(retirada)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 74, 153);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(retirada)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 74, 153);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)
        self.ln_justificativa = QtWidgets.QLineEdit(retirada)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ln_justificativa.setFont(font)
        self.ln_justificativa.setStyleSheet("border: 2px solid #bababa; /* borda cinza */\n"
"border-radius: 5px; \n"
"padding: 2 5px;\n"
"")
        self.ln_justificativa.setText("")
        self.ln_justificativa.setObjectName("ln_justificativa")
        self.gridLayout.addWidget(self.ln_justificativa, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(retirada)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 3, 0, 1, 1)

        self.retranslateUi(retirada)
        self.buttonBox.accepted.connect(retirada.accept) # type: ignore
        self.buttonBox.rejected.connect(retirada.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(retirada)

    def retranslateUi(self, retirada):
        _translate = QtCore.QCoreApplication.translate
        retirada.setWindowTitle(_translate("retirada", "Retirada de Amostras"))
        self.label_49.setText(_translate("retirada", "Retirada de Amostras"))
        self.label_5.setText(_translate("retirada", "Justificativa:"))
        self.chk_15dias.setText(_translate("retirada", " 15 dias - Excursão 1 (40ºC)"))
        self.chk_5dias.setText(_translate("retirada", " 5 dias - Excursão 2 (50ºC)"))
        self.label_6.setText(_translate("retirada", "Data retirada:"))
        self.label_8.setText(_translate("retirada", "Data retirada:"))
        self.label_7.setText(_translate("retirada", "Tipo de estudo:"))
        self.label_2.setText(_translate("retirada", "Qual amostra deseja retirar?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    retirada = QtWidgets.QDialog()
    ui = Ui_retirada()
    ui.setupUi(retirada)
    retirada.show()
    sys.exit(app.exec_())
