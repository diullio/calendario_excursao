# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView, QMenu, QAction, QApplication, QFileDialog
from PyQt5.QtCore import Qt, QAbstractTableModel, QDate, QPoint
from PyQt5.QtGui import QTextCharFormat, QColor
from datetime import datetime, timedelta
from unidecode import unidecode
import pandas as pd

class setarInicio():
    def __init__(self, main_window, Cadastro, UpdateCadastro, Registros, bd, usuario, directory_export, retirada):
        self.main_window = main_window
        self.gui = main_window.gui

        self.usuario = usuario

        self.Cadastro = Cadastro
        self.ui_Cadastro = Cadastro.Cadastro

        self.UpdateCadastro = UpdateCadastro
        self.ui_UpdateCadastro = UpdateCadastro.UpdateCadastro

        self.Registros = Registros
        self.ui_Registros = Registros.Registros

        self.retirada = retirada
        self.ui_retirada = retirada.retirada

        self.bd = bd
        self.directory_export = directory_export

        self.df_exportar = None

        self.startSystem()

    def startSystem(self):
        # try:
            self.botoesIniciais()
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    def botoesIniciais(self):
        # try:
            ##MAIN
            self.gui.date_inicial.setCalendarPopup(True)
            self.gui.date_inicial.setDate(datetime.now().date())
            self.gui.date_final.setCalendarPopup(True)
            self.gui.date_final.setDate(datetime.now().date() + timedelta(days=7))

            ##CADASTRO
            self.ui_Cadastro.date_cadastro.setCalendarPopup(True)
            self.ui_Cadastro.date_cadastro.setDate(datetime.now().date())

            ##UPDATE
            self.ui_UpdateCadastro.date_cadastro.setCalendarPopup(True)
            self.ui_UpdateCadastro.date_cadastro.setDate(datetime.now().date())

            ##REGISTRO
            self.ui_Registros.dateEdit.setCalendarPopup(True)
            self.ui_Registros.dateEdit.setDate(datetime.now().date())
            self.ui_Registros.dateEdit_2.setCalendarPopup(True)
            self.ui_Registros.dateEdit_2.setDate(datetime.now().date() + timedelta(days=7))

            self.ui_Registros.btn_busca_log.clicked.connect(self.fBuscaLOG)
            self.df_registro = None

            ##BOTOES
            self.gui.btn_cadastro.clicked.connect(self.showCadastro)
            self.gui.btn_registro.clicked.connect(self.showRegistro)
            self.gui.btn_buscar.clicked.connect(self.buscaCadastro)
            self.gui.btn_buscar.clicked.connect(self.consultaRetiradas)
            self.gui.tableView_agenda.doubleClicked.connect(self.showUpdateCadastro)
            self.gui.btn_exportar.clicked.connect(self.exportarDocumento)

            #botoes cadastro
            self.ui_Cadastro.btn_cadastro.clicked.connect(self.CadastrarInfos)
            self.ui_Cadastro.btn_cancelar.clicked.connect(self.CancelarCadastro)

            #botoes update
            self.id = None
            self.ui_UpdateCadastro.btn_cadastro.clicked.connect(self.UpdateInfos)
            self.ui_UpdateCadastro.btn_cancelar.clicked.connect(self.cancelarUpdate)

            ##CALENDARIO
            self.gui.calendarWidget.clicked.connect(self.buscar_dados)
            self.resetar_dias()
            self.colorir_dias_anteriores()
            self.colorir_dias_futuros()

            #RETIRADAS
            self.gui.btn_retirar_analise.clicked.connect(self.show_retiradas)
            self.ui_retirada.buttonBox.accepted.connect(self.selecionarRetirada)
            self.ui_retirada.buttonBox.rejected.connect(self.retirada.reject)

        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    ##CADASTRO
    def showCadastro(self):
        # try:
            self.Cadastro.exec_()          
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    def ajustar_data(self, data):
        # Se a data cair em um sábado (6) ou domingo (7), ajuste para segunda-feira
        while data.dayOfWeek() in (6, 7):
            data = data.addDays(1)
        return data
    
    def calcular_data_inicial_recomendada(self, data_ajustada, dias):
        data_recomendada = data_ajustada.addDays(-dias)
        while data_recomendada.dayOfWeek() in (6, 7):
            data_recomendada = data_recomendada.addDays(-1)
        return data_recomendada

    def LerInfosCadastro(self):
        # try:
            codigo = self.ui_Cadastro.ln_codigo.text()
            num_estudo = self.ui_Cadastro.ln_num_estudo.text()
            produto = self.ui_Cadastro.ln_produto.text()
            lote = self.ui_Cadastro.ln_lote.text()
            data_inicial = self.ui_Cadastro.date_cadastro.date()
            data = self.ui_Cadastro.date_cadastro.date().toString("yyyy-MM-dd")
            chk_5dias = self.ui_Cadastro.chk_5dias.isChecked()
            if chk_5dias:
                data_5_dias = data_inicial.addDays(4)
                data_5_dias_ajustada = self.ajustar_data(data_5_dias)
                if data_5_dias != data_5_dias_ajustada:
                    data_inicial_recomendada_5_dias = self.calcular_data_inicial_recomendada(data_5_dias_ajustada, 4)
                    QMessageBox.warning(None, "Ajuste de Data",
                                f"A data de retirada de 5 dias cai em um fim de semana.\n"
                                f"Data inicial recomendada: {data_inicial_recomendada_5_dias.toString('dd/MM/yyyy')}\n"
                                f"Data de retirada de 5 dias: {data_5_dias_ajustada.toString('dd/MM/yyyy')}")
                    return
                else:
                    chk_5dias = data_5_dias.toString('yyyy-MM-dd')
            chk_15dias = self.ui_Cadastro.chk_15dias.isChecked()
            if chk_15dias:
                data_15_dias = data_inicial.addDays(14)
                data_15_dias_ajustada = self.ajustar_data(data_15_dias)
                if data_15_dias != data_15_dias_ajustada:
                    data_inicial_recomendada_15_dias = self.calcular_data_inicial_recomendada(data_15_dias_ajustada, 14)
                    QMessageBox.warning(None, "Ajuste de Data",
                                f"A data de retirada de 15 dias cai em um fim de semana.\n"
                                f"Data inicial recomendada: {data_inicial_recomendada_15_dias.toString('dd/MM/yyyy')}\n"
                                f"Data de retirada de 15 dias: {data_15_dias_ajustada.toString('dd/MM/yyyy')}")
                    return
                else:
                    chk_15dias = data_15_dias.toString('yyyy-MM-dd')
            return codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias

        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")
    
    def LimparInfosCadastro(self):
        # try:
            self.ui_Cadastro.ln_codigo.clear()
            self.ui_Cadastro.ln_num_estudo.clear()
            self.ui_Cadastro.ln_produto.clear()
            self.ui_Cadastro.ln_lote.clear()
            self.ui_Cadastro.date_cadastro.setDate(datetime.now().date())
            self.ui_Cadastro.chk_5dias.setChecked(False)
            self.ui_Cadastro.chk_15dias.setChecked(False)
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}") 

    def format_date(self, data_str):
        # Converta a coluna de string para datetime, usando errors='coerce' para tratar valores nulos
        data_str = pd.to_datetime(data_str, format='%Y-%m-%d', errors='coerce')
        # Converta a coluna datetime para string no formato 'dd/mm/yyyy', mantendo NaT para valores nulos
        if pd.isnull(data_str):
            return '-'
        else:
            return data_str.strftime('%d/%m/%Y')

    def CadastrarInfos(self):
        # try:
            codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias = self.LerInfosCadastro()
            resultado = self.bd.query_cadastrar(codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias)
            if resultado == 'sucesso':
                QMessageBox.information(None, 'Concluído', 'Cadastro realizado com sucesso!')
                self.LimparInfosCadastro()
                self.Cadastro.reject()
                self.buscaCadastro()
                self.resetar_dias()
                self.colorir_dias_anteriores()
                self.colorir_dias_futuros()


                data = self.format_date(str(data))
                chk_5dias = self.format_date(str(chk_5dias))
                chk_15dias = self.format_date(str(chk_15dias))

                #Email:
                subject = f'Cadastro do estudo {num_estudo}'
                body = f"""
                Cadastro do estudo:

                Código: {codigo}
                Número de estudo: {num_estudo}
                Produto: {produto}
                Lote: {lote}
                Data de Cadastro: {data}
                Data de Retirada 5 dias: {chk_5dias}
                Data de Retirada 15 dias: {chk_15dias}

                Por: {self.usuario}

                """

                self.bd.enviarEmail(subject, body)
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}") 
    
    def converter_e_substituir_datas(self, df, coluna):
        # Converta a coluna de string para datetime, usando errors='coerce' para tratar valores nulos
        df[coluna] = pd.to_datetime(df[coluna], format='%Y-%m-%d', errors='coerce')
        # Converta a coluna datetime para string no formato 'dd/mm/yyyy', mantendo NaT para valores nulos
        df[coluna] = df[coluna].dt.strftime('%d/%m/%Y')
        return df

    def buscaCadastro(self):
        # try:    
            ln_num_estudo = self.gui.ln_num_estudo.text()
            ln_produto = self.gui.ln_produto.text()
            ln_lote = self.gui.ln_lote.text()
            data_inicial = self.gui.date_inicial.date().toString("yyyy-MM-dd")
            data_final = self.gui.date_final.date().toString("yyyy-MM-dd")
            
            df = self.bd.query_ConsultaCadastro(data_inicial, data_final, ln_num_estudo, ln_produto, ln_lote)
            self.df_consulta = df.copy()
            
            df = self.converter_e_substituir_datas(df, 'Data')
            df = self.converter_e_substituir_datas(df, '5 Dias')
            df = self.converter_e_substituir_datas(df, '15 Dias')
            df = df.replace({pd.NaT: '-', 'NaT': '-', '': '-', None: '-'})

            model = PandasModel(df)
            self.gui.tableView_agenda.setModel(model)
            self.gui.tableView_agenda.setSelectionMode(QAbstractItemView.SingleSelection)
            self.gui.tableView_agenda.resizeColumnsToContents()
            self.gui.tableView_agenda.setContextMenuPolicy(Qt.CustomContextMenu)
            self.gui.tableView_agenda.customContextMenuRequested.connect(self.open_menu)
        
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}") 

    def open_menu(self, position: QPoint):
        menu = QMenu()


        update_action = QAction("Atualizar", None)
        update_action.triggered.connect(self.showUpdateCadastro)
        menu.addAction(update_action)
            
        delete_action = QAction("Deletar", None)
        delete_action.triggered.connect(self.deletarCadastro)
        menu.addAction(delete_action)

        copy_action = QAction("Copiar", None)
        copy_action.triggered.connect(self.copy_selection)
        menu.addAction(copy_action)

        menu.exec_(self.gui.tableView_agenda.viewport().mapToGlobal(position))

    def copy_selection(self):
        # try:
        # Simula a ação de Ctrl+C
            selected_indexes = self.gui.tableView_agenda.selectionModel().selectedIndexes()
            if selected_indexes:
                index = selected_indexes[0]  # Como é seleção única, pegue o primeiro (e único) índice
                text = self.gui.tableView_agenda.model().data(index)
                QApplication.clipboard().setText(text)
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    def deletarCadastro(self):
        # try:
            selected_indexes = self.gui.tableView_agenda.selectionModel().selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                id = self.df_consulta.iloc[row]['ID']
                codigo = self.df_consulta.iloc[row]['Código']
                num_estudo = self.df_consulta.iloc[row]['Número de Estudo']
                produto = self.df_consulta.iloc[row]['Produto']
                lote = self.df_consulta.iloc[row]['Lote']
                data = self.df_consulta.iloc[row]['Data']
                chk_5dias = self.df_consulta.iloc[row]['5 Dias']
                chk_15dias = self.df_consulta.iloc[row]['15 Dias']
                id = int(id)

                #'ID', 'Código', 'Número de Estudo', 'Produto', 'Lote', 'Data', '5 Dias', '15 Dias', 'Usuário'

                confirm = QMessageBox.question(
                    None,
                    'Confirmação de Exclusão',
                    f'Tem certeza que deseja excluir o registro {id}?',
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )

                if confirm == QMessageBox.Yes:
                    resultado = self.bd.removerCadastro(id)
                    if resultado == 'sucesso':
                        QMessageBox.information(None, 'Concluído', 'Cadastro removido com sucesso!')
                        self.buscaCadastro()

                        data = self.format_date(str(data))
                        chk_5dias = self.format_date(str(chk_5dias))
                        chk_15dias = self.format_date(str(chk_15dias))

                        #Email:
                        subject = f'Cancelamento do estudo {num_estudo}'
                        body = f"""
                        Cancelamento de estudo:

                        Código: {codigo}
                        Número de estudo: {num_estudo}
                        Produto: {produto}
                        Lote: {lote}
                        Data de Cadastro: {data}
                        Data de Retirada 5 dias: {chk_5dias}
                        Data de Retirada 15 dias: {chk_15dias}

                        Por: {self.usuario}

                        """

                        self.bd.enviarEmail(subject, body)
                    else:
                        QMessageBox.information(None, 'Alerta', 'Erro ao remover cadastro, tente novamente!')
                        return
                else:
                    return
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    def CancelarCadastro(self):
        # try:
            self.LimparInfosCadastro()
            self.Cadastro.reject()          
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    ##UPDATE CADASTRO
    def showUpdateCadastro(self):
        # try:
            self.LimparInfosUpdate()
            self.setarInfosUpdate()
            self.UpdateCadastro.exec_()          
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    def setarInfosUpdate(self):
        # try:
            selected_indexes = self.gui.tableView_agenda.selectionModel().selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                id = self.df_consulta.iloc[row]['ID']
                self.id = int(id)

                id, codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias, usuario = self.bd.query_ConsultaUpdate(id)

                self.ui_UpdateCadastro.ln_codigo.setText(codigo)
                self.ui_UpdateCadastro.ln_num_estudo.setText(num_estudo)
                self.ui_UpdateCadastro.ln_produto.setText(produto)
                self.ui_UpdateCadastro.ln_lote.setText(lote)
                data_qdate = QDate.fromString(data, "yyyy-MM-dd")
                self.ui_UpdateCadastro.date_cadastro.setDate(data_qdate)
                if chk_5dias:
                    self.ui_UpdateCadastro.chk_5dias.setChecked(True)
                if chk_15dias:
                    self.ui_UpdateCadastro.chk_15dias.setChecked(True)
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")
    
    def LimparInfosUpdate(self):
        # try:
            self.id = None
            self.ui_UpdateCadastro.ln_codigo.clear()
            self.ui_UpdateCadastro.ln_num_estudo.clear()
            self.ui_UpdateCadastro.ln_produto.clear()
            self.ui_UpdateCadastro.ln_lote.clear()
            self.ui_UpdateCadastro.date_cadastro.setDate(datetime.now().date())
            self.ui_UpdateCadastro.chk_5dias.setChecked(False)
            self.ui_UpdateCadastro.chk_15dias.setChecked(False)
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}") 

    def LerInfosUpdate(self):
        # try:
            codigo = self.ui_UpdateCadastro.ln_codigo.text()
            num_estudo = self.ui_UpdateCadastro.ln_num_estudo.text()
            produto = self.ui_UpdateCadastro.ln_produto.text()
            lote = self.ui_UpdateCadastro.ln_lote.text()
            data_inicial = self.ui_UpdateCadastro.date_cadastro.date()
            data = self.ui_UpdateCadastro.date_cadastro.date().toString("yyyy-MM-dd")
            chk_5dias = self.ui_UpdateCadastro.chk_5dias.isChecked()
            if chk_5dias:
                data_5_dias = data_inicial.addDays(4)
                data_5_dias_ajustada = self.ajustar_data(data_5_dias)
                if data_5_dias != data_5_dias_ajustada:
                    data_inicial_recomendada_5_dias = self.calcular_data_inicial_recomendada(data_5_dias_ajustada, 4)
                    QMessageBox.warning(None, "Ajuste de Data",
                                f"A data de retirada de 5 dias cai em um fim de semana.\n"
                                f"Data inicial recomendada: {data_inicial_recomendada_5_dias.toString('dd/MM/yyyy')}\n"
                                f"Data de retirada de 5 dias: {data_5_dias_ajustada.toString('dd/MM/yyyy')}")
                    return
                else:
                    chk_5dias = data_5_dias.toString('yyyy-MM-dd')
            chk_15dias = self.ui_UpdateCadastro.chk_15dias.isChecked()
            if chk_15dias:
                data_15_dias = data_inicial.addDays(14)
                data_15_dias_ajustada = self.ajustar_data(data_15_dias)
                if data_15_dias != data_15_dias_ajustada:
                    data_inicial_recomendada_15_dias = self.calcular_data_inicial_recomendada(data_15_dias_ajustada, 14)
                    QMessageBox.warning(None, "Ajuste de Data",
                                f"A data de retirada de 15 dias cai em um fim de semana.\n"
                                f"Data inicial recomendada: {data_inicial_recomendada_15_dias.toString('dd/MM/yyyy')}\n"
                                f"Data de retirada de 15 dias: {data_15_dias_ajustada.toString('dd/MM/yyyy')}")
                    return
                else:
                    chk_15dias = data_15_dias.toString('yyyy-MM-dd')

            return codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias

        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    def UpdateInfos(self):
        # try:
            id = self.id
            id = int(id)
            if not id:
                QMessageBox.information(None, 'Alerta', 'ID inválido, tente novamente!')
                return

            codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias = self.LerInfosUpdate()
            resultado = self.bd.query_update(id, codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias)
            if resultado == 'sucesso':
                QMessageBox.information(None, 'Concluído', 'Cadastro atualizado com sucesso!')
                self.LimparInfosUpdate()
                self.UpdateCadastro.reject()
                self.buscaCadastro()
                self.resetar_dias()
                self.colorir_dias_anteriores()
                self.colorir_dias_futuros()
                #Email:

                data = self.format_date(str(data))
                chk_5dias = self.format_date(str(chk_5dias))
                chk_15dias = self.format_date(str(chk_15dias))

                subject = f'Atualização do estudo {num_estudo}'
                body = f"""
                Atualização de estudo:

                Código: {codigo}
                Número de estudo: {num_estudo}
                Produto: {produto}
                Lote: {lote}
                Data de Cadastro: {data}
                Data de Retirada 5 dias: {chk_5dias}
                Data de Retirada 15 dias: {chk_15dias}

                Por: {self.usuario}

                """

                self.bd.enviarEmail(subject, body)
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}") 
    
    def cancelarUpdate(self):
        # try:
            self.LimparInfosUpdate()
            self.UpdateCadastro.reject()          
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")
    
    ##CONSULTAS
    def buscar_dados(self):
        # try:
            data = self.gui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
            df = self.bd.consultaCalendario(data)

            self.df_consulta = df.copy()

            df = self.converter_e_substituir_datas(df, 'Data')
            df = self.converter_e_substituir_datas(df, '5 Dias')
            df = self.converter_e_substituir_datas(df, '15 Dias')
            df = df.replace({pd.NaT: '-', 'NaT': '-', '': '-', None: '-'})

            self.df_exportar = df.copy()
            model = PandasModel(df)
            self.gui.tableView_agenda.setModel(model)
            self.gui.tableView_agenda.setSelectionMode(QAbstractItemView.SingleSelection)
            self.gui.tableView_agenda.resizeColumnsToContents()
            self.gui.tableView_agenda.setContextMenuPolicy(Qt.CustomContextMenu)
            self.gui.tableView_agenda.customContextMenuRequested.connect(self.open_menu)
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")    

    def directory_export(self):
            options = QFileDialog.Options()
            options |= QFileDialog.ShowDirsOnly
            folder_path = QFileDialog.getExistingDirectory(self, "Selecionar Pasta", options=options)
            return folder_path
    
    def exportarDocumento(self):
        try:
            if self.df_exportar:
                self.folder_path = self.directory_export() 
                if self.folder_path:
                    data_e_hora_atual = datetime.now().strftime('%Y%m%d_%H%M%S')
                    # Gerando o nome do arquivo com base na data e hora
                    nome_arquivo = f"excursao_{data_e_hora_atual}.xlsx"

                    caminho_arquivo = os.path.join(self.folder_path, nome_arquivo)            
                    self.df_exportar.to_excel(caminho_arquivo, index=False)
        except:
            QMessageBox.information(None, 'Alerta', "Dados invalidos, selecione uma nova data")
            return None

    def resetar_dias(self):
         # Formato de texto para resetar as datas para branco
        format_white_background = QTextCharFormat()
        format_white_background.setBackground(QColor("white"))

        # Itera sobre todas as datas do ano atual e define a cor de fundo para branco
        current_year = QDate.currentDate().year()
        for month in range(1, 13):
            for day in range(1, 32):
                # try:
                    qdate = QDate(current_year, month, day)
                    if qdate.isValid():
                        self.gui.calendarWidget.setDateTextFormat(qdate, format_white_background)
                # except ValueError:
                #     pass

    def colorir_dias_anteriores(self):
        data_hoje = QDate.currentDate().toString("yyyy-MM-dd")

        # Formato de texto para colorir as datas
        format_red_background = QTextCharFormat()
        format_red_background.setBackground(QColor("red"))

        datas_anteriores_5 = self.bd.buscarDatasAnteriores_5(data_hoje)
        # Itera sobre as datas e colore os dias no calendário
        for data in datas_anteriores_5:
            date_str = data[0]
            if isinstance(date_str, str):
                qdate = QDate.fromString(date_str, "yyyy-MM-dd")
                if qdate.isValid():
                    self.gui.calendarWidget.setDateTextFormat(qdate, format_red_background)

        datas_anteriores_15 = self.bd.buscarDatasAnteriores_15(data_hoje)
        # Itera sobre as datas e colore os dias no calendário
        for data in datas_anteriores_15:
            date_str = data[0]
            if isinstance(date_str, str):
                qdate = QDate.fromString(date_str, "yyyy-MM-dd")
                if qdate.isValid():
                    self.gui.calendarWidget.setDateTextFormat(qdate, format_red_background)

    def colorir_dias_futuros(self):
        data_hoje = QDate.currentDate().toString("yyyy-MM-dd")

        # Formato de texto para colorir as datas
        format_green_background = QTextCharFormat()
        format_green_background.setBackground(QColor("green"))

        datas_futuras_5 = self.bd.buscarDatasFuturas_5(data_hoje)
        # Itera sobre as datas e colore os dias no calendário
        for data in datas_futuras_5:
            date_str = data[0]
            if isinstance(date_str, str):
                qdate = QDate.fromString(data[0], "yyyy-MM-dd")
                if qdate.isValid():
                    self.gui.calendarWidget.setDateTextFormat(qdate, format_green_background)

        datas_futuras_15 = self.bd.buscarDatasFuturas_15(data_hoje)
        # Itera sobre as datas e colore os dias no calendário
        # Itera sobre as datas e colore os dias no calendário
        for data in datas_futuras_15:
            date_str = data[0]
            if isinstance(date_str, str):
                qdate = QDate.fromString(data[0], "yyyy-MM-dd")
                if qdate.isValid():
                    self.gui.calendarWidget.setDateTextFormat(qdate, format_green_background)

    ##AMOSTRAS RETIRADAS
    def show_retiradas(self):
        # try:
            self.LimparInfosRetirada()
            self.setarRetirarAmostras()
            self.retirada.exec_()
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    def selecionarRetirada(self):
        # try:
            selected_indexes = self.gui.tableView_agenda.selectionModel().selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                id = self.df_consulta.iloc[row]['ID']
                id = int(id)
                codigo = self.df_consulta.iloc[row]['Código']
                num_estudo = self.df_consulta.iloc[row]['Número de Estudo']
                produto = self.df_consulta.iloc[row]['Produto']
                lote = self.df_consulta.iloc[row]['Lote']
                data = self.df_consulta.iloc[row]['Data']

                chk_5data = self.df_consulta.iloc[row]['5 Dias']
                chk_15data = self.df_consulta.iloc[row]['15 Dias']

                chk_5d = self.ui_retirada.chk_5dias.isChecked()
                chk_15d = self.ui_retirada.chk_15dias.isChecked()
                ln_justificativa = self.ui_retirada.ln_justificativa.text()

                data_hoje = QDate.currentDate().toString('yyyy-MM-dd')
                data_hoje = pd.to_datetime(data_hoje, format='%Y-%m-%d')

                # Checando a condição de chk_5dias
                if chk_5d:
                    chk_5data = pd.to_datetime(chk_5data, format='%y-%m-%d', errors='coerce')
                    if chk_5data != data_hoje and not ln_justificativa:
                        QMessageBox.information(None, 'Alerta', "Justificativa é obrigatória para data diferente de hoje!")
                        return

                 # Checando a condição de chk_15dias
                if chk_15d:
                    chk_15data = pd.to_datetime(chk_15data, format='%y-%m-%d', errors='coerce')
                    if chk_15data != data_hoje and not ln_justificativa:
                        QMessageBox.information(None, 'Alerta', "Justificativa é obrigatória para data diferente de hoje!")
                        return

                resultado = self.bd.retirarAmostra(id, chk_5d, chk_15d, ln_justificativa)
                if resultado == 'sucesso':
                    QMessageBox.information(None, 'Concluído', 'Amostra retirada com sucesso!')
                    self.LimparInfosRetirada()
                    self.retirada.reject()
                    self.buscaCadastro()
                    self.resetar_dias()
                    self.colorir_dias_anteriores()
                    self.colorir_dias_futuros()
                    self.consultaRetiradas()
                    #Email:

                    data = self.format_date(str(data))
                    chk_5data = self.format_date(str(chk_5data))
                    chk_15data = self.format_date(str(chk_15data))
                    data_hoje = self.format_date(str(data_hoje))

                    subject = f'Retirada do estudo {num_estudo} para análise'
                    body = f"""
                    Retirada de estudo para análise:

                    Código: {codigo}
                    Número de estudo: {num_estudo}
                    Produto: {produto}
                    Lote: {lote}
                    Data de Cadastro: {data}
                    Data de Retirada em 5 dias: {chk_5data}
                    Data de Retirada em 15 dias: {chk_15data}

                    Amostra Retirada:
                    """

                    if chk_5d:
                        body += f"""
                    Amostra 5 dias: '{data_hoje}'
                    """

                    if chk_5d and ln_justificativa:
                        body += f"""
                    Justificativa: {ln_justificativa}
                    """

                    if chk_15d:
                        body += f"""
                    Amostra 15 dias: '{data_hoje}'
                    """

                    if chk_15d and ln_justificativa:
                        body += f"""
                    Justificativa: {ln_justificativa}
                    """

                    body += f"""

                    Por: {self.usuario}
                    """

                    self.bd.enviarEmail(subject, body)
                else:
                    QMessageBox.information(None, 'Alerta', 'Amostra já foi retirada!')
                    return

        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")
    
    def consultaRetiradas(self):
        # try:
            ln_num_estudo = self.gui.ln_num_estudo.text()
            ln_produto = self.gui.ln_produto.text()
            ln_lote = self.gui.ln_lote.text()
            data_inicial = self.gui.date_inicial.date().toString("yyyy-MM-dd")
            data_final = self.gui.date_final.date().toString("yyyy-MM-dd")
            
            df = self.bd.consultaRetiradas(data_inicial, data_final, ln_num_estudo, ln_produto, ln_lote)

            df = self.converter_e_substituir_datas(df, 'Data')
            df = self.converter_e_substituir_datas(df, '5 Dias')
            df = self.converter_e_substituir_datas(df, '15 Dias')
            df = self.converter_e_substituir_datas(df, 'Retirada 5 Dias')
            df = self.converter_e_substituir_datas(df, 'Retirada 15 Dias')
            df = df.replace({pd.NaT: '-', 'NaT': '-', '': '-', None: '-'})

            model = PandasModel(df)
            self.gui.tableView_retirados.setModel(model)
            self.gui.tableView_retirados.setSelectionMode(QAbstractItemView.SingleSelection)
            self.gui.tableView_retirados.resizeColumnsToContents()
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    def LimparInfosRetirada(self):
        # try:
            self.ui_retirada.ln_retirada_5.setReadOnly(True)
            self.ui_retirada.chk_5dias.setChecked(False)
            self.ui_retirada.ln_retirada_15.setReadOnly(True)
            self.ui_retirada.chk_15dias.setChecked(False)
            self.ui_retirada.ln_justificativa.clear()
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    def setarRetirarAmostras(self):
        # try:
            selected_indexes = self.gui.tableView_agenda.selectionModel().selectedIndexes()
            if selected_indexes:
                row = selected_indexes[0].row()
                chk_5d = self.df_consulta.iloc[row]['5 Dias']
                chk_15d = self.df_consulta.iloc[row]['15 Dias']
                
                if chk_5d:
                    chk_5d = self.format_date(chk_5d)
                    self.ui_retirada.ln_retirada_5.setText(str(chk_5d))
                else:
                    self.ui_retirada.ln_retirada_5.setText('')
                if chk_15d:
                    chk_15d = self.format_date(chk_15d)
                    self.ui_retirada.ln_retirada_15.setText(str(chk_15d))
                else:
                    self.ui_retirada.ln_retirada_15.setText('')
            else:
                QMessageBox.information(None, 'Alerta', 'Selecione uma amostra para retirar para análise')
                return
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")

    ##AUDITORIA
    def showRegistro(self):
        # try:
            self.Registros.exec_()          
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")
        
    def fBuscaLOG(self):
        # try:
            usuario = self.ui_Registros.users_log.text()
            if usuario:
                usuario = usuario.lower()
                usuario = unidecode(usuario)
            selected_date = self.ui_Registros.dateEdit.date().toString("yyyy-MM-dd")
            selected_date_fim = self.ui_Registros.dateEdit_2.date().toString("yyyy-MM-dd")
            texto = self.ui_Registros.ln_buscarRegistro.text()
            df = self.bd.selecionarLOG(selected_date, selected_date_fim, usuario, texto)

            df.sort_values(by='Id', ascending=False, inplace=True)
            self.df = df.copy()
            
            model = PandasModel(df)
            self.ui_Registros.tableView_LOG.setModel(model)
            self.ui_Registros.tableView_LOG.resizeColumnsToContents()
        # except Exception as e:
        #     print(f"Ocorreu uma exceção: {e}")


class PandasModel(QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
