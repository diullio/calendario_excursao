# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cadastro.setStyleSheet("QPushButton {\n"
"                border: 2px solid #004a99; /* borda azul */\n"
"                border-radius: 5px; /* bordas mais quadradas */\n"
"                color: #004a99; /* fonte azul */\n"
"                padding:3px 10px;\n"
"            }\n"
"QPushButton:hover {\n"
"                background-color: #004a99; /* hover azul */\n"
"                color: #ffffff; /* fonte branca */\n"
"            }")
        self.btn_cadastro.setObjectName("btn_cadastro")
        self.gridLayout.addWidget(self.btn_cadastro, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.btn_registro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registro.setStyleSheet("QPushButton {\n"
"                border: 2px solid #004a99; /* borda azul */\n"
"                border-radius: 5px; /* bordas mais quadradas */\n"
"                color: #004a99; /* fonte azul */\n"
"                padding:3px 10px;\n"
"            }\n"
"QPushButton:hover {\n"
"                background-color: #004a99; /* hover azul */\n"
"                color: #ffffff; /* fonte branca */\n"
"            }")
        self.btn_registro.setObjectName("btn_registro")
        self.gridLayout.addWidget(self.btn_registro, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.gridGroupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.gridGroupBox_3.setObjectName("gridGroupBox_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridGroupBox_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.gridGroupBox_3)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_11.addWidget(self.calendarWidget, 1, 0, 1, 1)
        self.tableView_agenda = QtWidgets.QTableView(self.gridGroupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableView_agenda.setFont(font)
        self.tableView_agenda.setStyleSheet("")
        self.tableView_agenda.setObjectName("tableView_agenda")
        self.gridLayout_11.addWidget(self.tableView_agenda, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_retirar_analise = QtWidgets.QPushButton(self.gridGroupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_retirar_analise.setFont(font)
        self.btn_retirar_analise.setStyleSheet("QPushButton {\n"
"                border: 2px solid #004a99; /* borda azul */\n"
"                border-radius: 5px; /* bordas mais quadradas */\n"
"                color: rgb(255, 255, 255); /* fonte azul */\n"
"                padding:3px 10px;\n"
"    background-color: rgb(0, 74, 153);\n"
"            }\n"
"QPushButton:hover {\n"
"                background-color: rgb(255, 255, 255); /* hover azul */\n"
"                color: rgb(0, 74, 153); /* fonte branca */\n"
"            }")
        self.btn_retirar_analise.setObjectName("btn_retirar_analise")
        self.gridLayout_3.addWidget(self.btn_retirar_analise, 0, 0, 1, 1)
        self.btn_exportar = QtWidgets.QPushButton(self.gridGroupBox_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_exportar.setFont(font)
        self.btn_exportar.setStyleSheet("QPushButton {\n"
"                border: 2px solid #004a99; /* borda azul */\n"
"                border-radius: 5px; /* bordas mais quadradas */\n"
"                color: rgb(255, 255, 255); /* fonte azul */\n"
"                padding:3px 10px;\n"
"    background-color: rgb(0, 74, 153);\n"
"            }\n"
"QPushButton:hover {\n"
"                background-color: rgb(255, 255, 255); /* hover azul */\n"
"                color: rgb(0, 74, 153); /* fonte branca */\n"
"            }")
        self.btn_exportar.setObjectName("btn_exportar")
        self.gridLayout_3.addWidget(self.btn_exportar, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_3, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.gridGroupBox_3, 5, 0, 1, 2)
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
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
        self.gridLayout_2.addWidget(self.label_49, 0, 0, 1, 2)
        self.gridGroupBox_13 = QtWidgets.QGroupBox(self.centralwidget)
        self.gridGroupBox_13.setObjectName("gridGroupBox_13")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.gridGroupBox_13)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.label_139 = QtWidgets.QLabel(self.gridGroupBox_13)
        self.label_139.setText("")
        self.label_139.setObjectName("label_139")
        self.gridLayout_37.addWidget(self.label_139, 0, 15, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridGroupBox_13)
        self.label_34.setObjectName("label_34")
        self.gridLayout_37.addWidget(self.label_34, 0, 9, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridGroupBox_13)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 74, 153);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_37.addWidget(self.label_5, 0, 6, 1, 1)
        self.ln_lote = QtWidgets.QLineEdit(self.gridGroupBox_13)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ln_lote.setFont(font)
        self.ln_lote.setStyleSheet("border: 2px solid #bababa; /* borda cinza */\n"
"border-radius: 5px; \n"
"padding: 2 5px;\n"
"")
        self.ln_lote.setText("")
        self.ln_lote.setObjectName("ln_lote")
        self.gridLayout_37.addWidget(self.ln_lote, 0, 7, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem3, 0, 11, 1, 1)
        self.date_final = QtWidgets.QDateEdit(self.gridGroupBox_13)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.date_final.setFont(font)
        self.date_final.setStyleSheet("")
        self.date_final.setObjectName("date_final")
        self.gridLayout_37.addWidget(self.date_final, 0, 13, 1, 1)
        self.ln_num_estudo = QtWidgets.QLineEdit(self.gridGroupBox_13)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ln_num_estudo.setFont(font)
        self.ln_num_estudo.setStyleSheet("border: 2px solid #bababa; /* borda cinza */\n"
"border-radius: 5px; \n"
"padding: 2 5px;\n"
"")
        self.ln_num_estudo.setText("")
        self.ln_num_estudo.setObjectName("ln_num_estudo")
        self.gridLayout_37.addWidget(self.ln_num_estudo, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridGroupBox_13)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 74, 153);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_37.addWidget(self.label_4, 0, 3, 1, 1)
        self.ln_produto = QtWidgets.QLineEdit(self.gridGroupBox_13)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ln_produto.setFont(font)
        self.ln_produto.setStyleSheet("border: 2px solid #bababa; /* borda cinza */\n"
"border-radius: 5px; \n"
"padding: 2 5px;\n"
"")
        self.ln_produto.setText("")
        self.ln_produto.setObjectName("ln_produto")
        self.gridLayout_37.addWidget(self.ln_produto, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridGroupBox_13)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 74, 153);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_37.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_138 = QtWidgets.QLabel(self.gridGroupBox_13)
        self.label_138.setObjectName("label_138")
        self.gridLayout_37.addWidget(self.label_138, 0, 12, 1, 1)
        self.btn_buscar = QtWidgets.QPushButton(self.gridGroupBox_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_buscar.sizePolicy().hasHeightForWidth())
        self.btn_buscar.setSizePolicy(sizePolicy)
        self.btn_buscar.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_buscar.setStyleSheet("QPushButton {\n"
"                border: 2px solid #004a99; /* borda azul */\n"
"                border-radius: 5px; /* bordas mais quadradas */\n"
"                color: rgb(255, 255, 255); /* fonte azul */\n"
"                padding:3px 10px;\n"
"    background-color: rgb(0, 74, 153);\n"
"            }\n"
"QPushButton:hover {\n"
"                background-color: rgb(255, 255, 255); /* hover azul */\n"
"                color: rgb(0, 74, 153); /* fonte branca */\n"
"            }")
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout_37.addWidget(self.btn_buscar, 0, 16, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem4, 0, 8, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem5, 0, 14, 1, 1)
        self.date_inicial = QtWidgets.QDateEdit(self.gridGroupBox_13)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.date_inicial.setFont(font)
        self.date_inicial.setStyleSheet("")
        self.date_inicial.setObjectName("date_inicial")
        self.gridLayout_37.addWidget(self.date_inicial, 0, 10, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem6, 0, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem7, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.gridGroupBox_13, 3, 0, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 10, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem9, 4, 1, 1, 1)
        self.gridGroupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.gridGroupBox_4.setStyleSheet("")
        self.gridGroupBox_4.setObjectName("gridGroupBox_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridGroupBox_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.tableView_retirados = QtWidgets.QTableView(self.gridGroupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableView_retirados.setFont(font)
        self.tableView_retirados.setStyleSheet("")
        self.tableView_retirados.setObjectName("tableView_retirados")
        self.gridLayout_12.addWidget(self.tableView_retirados, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gridGroupBox_4, 9, 0, 1, 2)
        self.label_137 = QtWidgets.QLabel(self.centralwidget)
        self.label_137.setObjectName("label_137")
        self.gridLayout_2.addWidget(self.label_137, 8, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Estabilidade de Excursão"))
        self.btn_cadastro.setText(_translate("MainWindow", "Cadastro"))
        self.btn_registro.setText(_translate("MainWindow", "Auditoria"))
        self.btn_retirar_analise.setText(_translate("MainWindow", "Retirar para análise"))
        self.btn_exportar.setText(_translate("MainWindow", "Exportar"))
        self.label_49.setText(_translate("MainWindow", "Estabilidade de excursão"))
        self.label_34.setText(_translate("MainWindow", "De:"))
        self.label_5.setText(_translate("MainWindow", "Lote:"))
        self.label_4.setText(_translate("MainWindow", "Produto"))
        self.label_3.setText(_translate("MainWindow", "Nº de Estudo:"))
        self.label_138.setText(_translate("MainWindow", "Até:"))
        self.btn_buscar.setText(_translate("MainWindow", "Buscar"))
        self.label_137.setText(_translate("MainWindow", "Amostras retiradas:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
