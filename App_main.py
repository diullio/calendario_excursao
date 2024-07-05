# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QFileDialog
import getpass
from datetime import datetime

ABSOLUT_PATH = os.path.dirname(os.path.realpath(__file__))
interface_path = os.path.join(ABSOLUT_PATH, 'interface')
functions_path = os.path.join(ABSOLUT_PATH, 'functions')
database_path = os.path.join(ABSOLUT_PATH, 'database')

from interface.gui_main import Ui_MainWindow
from interface.gui_atualizar_cadastro import Ui_Dialog as Ui_UpdateCadastro
from interface.gui_cadastro import Ui_Dialog as Ui_Cadastro
from interface.gui_registros import Ui_Registros
from interface.gui_retiradas import Ui_retirada

from functions.home import setarInicio
from functions.bd import bd

class FrontEnd(QMainWindow, QDialog):
    def __init__(self):
        super(FrontEnd, self).__init__()
        self.usuario = getpass.getuser()
        self.data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    #GUI - interface
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.showMaximized()

    #Dialogos
        self.Cadastro = Cadastro()
        self.ui_Cadastro = self.Cadastro.Cadastro

        self.UpdateCadastro = UpdateCadastro()
        self.ui_UpdateCadastro = self.UpdateCadastro.UpdateCadastro

        self.Registros = Registros()
        self.ui_Registros = self.Registros.Registros

        self.retirada = retirada()
        self.ui_retirada = self.retirada.retirada

        self.bd = bd(self.usuario)

    #Funções -- INICIO - LOGIN E PERMISSOES
        self.setarInicio = setarInicio(self, self.Cadastro, self.UpdateCadastro, self.Registros, self.bd, self.usuario, self.directory_export, self.retirada)

    def directory_export(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        folder_path = QFileDialog.getExistingDirectory(self, "Selecionar Pasta", options=options)
        return folder_path

## FECHAR PROGRAMA
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Encerrar', 'Você realmente deseja sair?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()

class Cadastro(QDialog):
    def __init__(self):
        super(Cadastro, self).__init__()
        self.Cadastro = Ui_Cadastro()
        self.Cadastro.setupUi(self)

    def closeEvent(self, event):
        event.accept()  

class UpdateCadastro(QDialog):
    def __init__(self):
        super(UpdateCadastro, self).__init__()
        self.UpdateCadastro = Ui_UpdateCadastro()
        self.UpdateCadastro.setupUi(self)

    def closeEvent(self, event):
        event.accept()  

class Registros(QDialog):
    def __init__(self):
        super(Registros, self).__init__()
        self.Registros = Ui_Registros()
        self.Registros.setupUi(self)

    def closeEvent(self, event):
        event.accept() 
         
class retirada(QDialog):
    def __init__(self):
        super(retirada, self).__init__()
        self.retirada = Ui_retirada()
        self.retirada.setupUi(self)

    def closeEvent(self, event):
        event.accept()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = FrontEnd()
    gui.show() 
    sys.exit(app.exec_())
        

