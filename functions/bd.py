# -*- coding: utf-8 -*-
import os
import sqlite3
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

script_dir = os.path.dirname(os.path.abspath(__file__))
ABSOLUT_PATH = os.path.join(script_dir, '..')
database_path = os.path.join(ABSOLUT_PATH, 'database')

class bd():
    def __init__(self, usuario):
        print('Estabilidade de Excursão')
    
        self.diretorio = os.path.join(database_path, 'database.db')
        self.usuario = usuario
        self.inserir_registros(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"Sistema iniciado por {self.usuario}", self.usuario)

        ##CADASTRAR
    def query_cadastrar(self, codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()

            c.execute('''
                    INSERT INTO excursao (codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias, usuario)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias, self.usuario))

            conn.commit()
            last_id = c.lastrowid

            return 'sucesso'
                
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()
                self.inserir_registros(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"Inserção de cadastro: ID: {last_id}, Código: {codigo}, Número de Estudo: {num_estudo}, Produto: {produto}, Lote: {lote}, Data: {data}, 5 dias: {chk_5dias}, 15 Dias: {chk_15dias}, Usuário:{self.usuario}", self.usuario)
        
    def query_ConsultaCadastro(self, date_inicio, date_fim, ln_num_estudo, ln_produto, ln_lote):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()

            # Parâmetros da consulta
            params = []
            query = """
                SELECT id, codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias, usuario 
                FROM excursao 
                WHERE (data_retirada_5 IS NULL OR data_retirada_15 IS NULL)
            """
            
            # Adiciona filtros dinâmicos
            if ln_num_estudo:
                query += " AND num_estudo LIKE ?"
                params.append(f'%{ln_num_estudo}%')
            if ln_produto:
                query += " AND produto LIKE ?"
                params.append(f'%{ln_produto}%')
            if ln_lote:
                query += " AND lote LIKE ?"
                params.append(f'%{ln_lote}%')
            
            # Adiciona filtro de data
            query += " AND (data BETWEEN ? AND ? OR chk_5dias BETWEEN ? AND ? OR chk_15dias BETWEEN ? AND ?)"
            params.extend([date_inicio, date_fim, date_inicio, date_fim, date_inicio, date_fim])
            
            # Executa a consulta
            c.execute(query, params)
            registros = c.fetchall()

            # Cria o DataFrame com os resultados
            df = pd.DataFrame(registros, columns=[
                'ID', 'Código', 'Número de Estudo', 'Produto', 'Lote', 'Data', 
                '5 Dias', '15 Dias', 'Usuário'
            ]) if registros else pd.DataFrame(columns=[
                'ID', 'Código', 'Número de Estudo', 'Produto', 'Lote', 'Data', 
                '5 Dias', '15 Dias', 'Usuário'
            ])

            return df
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()


    def query_ConsultaUpdate(self, id):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            id = int(id)
            
            # Consultar se o usuário já existe na tabela de login
            sqlite_select_query = f"SELECT id, codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias, usuario FROM excursao WHERE id = ?"
            c.execute(sqlite_select_query, (id,))
            registros = c.fetchone()
            return registros
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()

    def removerCadastro(self, id):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            id = int(id)
            # Construa a string SQL para exclusão
            sql_delete = """
            DELETE FROM excursao
            WHERE id = ?
            """
            # Execute a exclusão no banco de dados
            c.execute(sql_delete, (id,))
            conn.commit()
            return 'sucesso'
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
            return None
        finally:
            if conn:
                conn.close()
                self.inserir_registros(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"Remoção do cadastro ID: {id}, Usuário:{self.usuario}", self.usuario)

    def query_update(self, id, codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            id = int(id)

            # atualizar dados na tabela 
            c.execute('''
                    UPDATE excursao SET codigo = ?, num_estudo = ?, produto = ?, lote = ?, data = ?, chk_5dias = ?, chk_15dias = ?, usuario = ? WHERE id = ?
                ''', (codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias, self.usuario, id))
            
            conn.commit()
            return 'sucesso'
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()
                self.inserir_registros(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"Atualização de cadastro: ID: {id}, Código: {codigo}, Número de Estudo: {num_estudo}, Produto: {produto}, Lote: {lote}, Data: {data}, 5 dias: {chk_5dias}, 15 Dias: {chk_15dias}, Usuário:{self.usuario}", self.usuario)

    def consultaCalendario(self, data):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            
            # Consultar se o usuário já existe na tabela de login
            sqlite_select_query = f"""SELECT id, codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias, usuario 
            FROM excursao 
            WHERE data = ? OR chk_5dias = ? OR chk_15dias = ?"""
            c.execute(sqlite_select_query, (data, data, data))
            registros = c.fetchall()

            if registros:
                df = pd.DataFrame(registros, columns=['ID', 'Código', 'Número de Estudo', 'Produto', 'Lote', 'Data', '5 Dias', '15 Dias', 'Usuário'])
            else:
                df = pd.DataFrame(columns=['ID', 'Código', 'Número de Estudo', 'Produto', 'Lote', 'Data', '5 Dias', '15 Dias', 'Usuário'])
            return df
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()

    def buscarDatasAnteriores_5(self, data):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            
            sqlite_select_query = f"SELECT chk_5dias FROM excursao WHERE chk_5dias < ? AND data_retirada_5 IS NULL"
            c.execute(sqlite_select_query, (data, ))
            datas_anteriores = c.fetchall()

            return datas_anteriores
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()

    def buscarDatasAnteriores_15(self, data):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            
            sqlite_select_query = f"SELECT chk_15dias FROM excursao WHERE chk_15dias < ? AND data_retirada_15 IS NULL"
            c.execute(sqlite_select_query, (data, ))
            datas_anteriores = c.fetchall()

            return datas_anteriores
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()
                
    def buscarDatasFuturas_5(self, data):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            
            sqlite_select_query = f"SELECT chk_5dias FROM excursao WHERE chk_5dias >= ? AND data_retirada_5 IS NULL"
            c.execute(sqlite_select_query, (data, ))
            datas_futuras = c.fetchall()

            return datas_futuras
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()

    def buscarDatasFuturas_15(self, data):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            
            sqlite_select_query = f"SELECT chk_15dias FROM excursao WHERE chk_15dias >= ? AND data_retirada_15 IS NULL"
            c.execute(sqlite_select_query, (data, ))
            datas_futuras = c.fetchall()

            return datas_futuras
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()

    def retirarAmostra(self, id, chk_5d, chk_15d, justificativa):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            id = int(id)

            if chk_5d:
                sqlite_select_query = 'SELECT data_retirada_5 FROM excursao WHERE id = ?'
                c.execute(sqlite_select_query, (id, ))
                racional = c.fetchone()
                if racional[0]:
                    return 'existe'
                else:
                    # atualizar dados na tabela
                    c.execute('''
                            UPDATE excursao SET data_retirada_5 = ?, analista_retirada_5 = ?, justificativa_5d = ? WHERE id = ?
                        ''', (datetime.now().strftime("%Y-%m-%d"), self.usuario, justificativa, id))
            if chk_15d:
                sqlite_select_query = 'SELECT data_retirada_15 FROM excursao WHERE id = ?'
                c.execute(sqlite_select_query, (id, ))
                racional = c.fetchone()
                if racional[0]:
                    return 'existe'
                else:
                # atualizar dados na tabela 
                    c.execute('''
                            UPDATE excursao SET data_retirada_15 = ?, analista_retirada_15 = ?, justificativa_15d = ? WHERE id = ?
                        ''', (datetime.now().strftime("%Y-%m-%d"), self.usuario, justificativa, id))
                
            conn.commit()
            return 'sucesso'
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()
                self.inserir_registros(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"Retirada de amostra: 5 dias: {chk_5d}, 15 dias: {chk_15d}", self.usuario)

    def consultaRetiradas(self,data_inicial, data_final, ln_num_estudo, ln_produto, ln_lote):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()

            # Parâmetros da consulta
            params = []
            query = """
                SELECT id, codigo, num_estudo, produto, lote, data, chk_5dias, chk_15dias, usuario, data_retirada_5, analista_retirada_5, data_retirada_15, analista_retirada_15, justificativa_5d, justificativa_15d
                FROM excursao 
                WHERE (data_retirada_5 IS NOT NULL OR data_retirada_15 IS NOT NULL)
            """
            
            # Adiciona filtros dinâmicos
            if ln_num_estudo:
                query += " AND num_estudo LIKE ?"
                params.append(f'%{ln_num_estudo}%')
            if ln_produto:
                query += " AND produto LIKE ?"
                params.append(f'%{ln_produto}%')
            if ln_lote:
                query += " AND lote LIKE ?"
                params.append(f'%{ln_lote}%')
            
            # Adiciona filtro de data
            query += " AND (data BETWEEN ? AND ? OR chk_5dias BETWEEN ? AND ? OR chk_15dias BETWEEN ? AND ?)"
            params.extend([data_inicial, data_final, data_inicial, data_final, data_inicial, data_final])
            
            # Executa a consulta
            c.execute(query, params)
            registros = c.fetchall()
            if registros:
                df = pd.DataFrame(registros, columns=['ID', 'Código', 'Número de Estudo', 'Produto', 'Lote', 'Data', '5 Dias', '15 Dias', 'Usuário', 'Retirada 5 Dias', 'Analista 5 Dias', 'Retirada 15 Dias', 'Analista 15 Dias', 'Justificativa 5 dias',  'Justificativa 15 dias'])
            else:
                df = pd.DataFrame(columns=['ID', 'Código', 'Número de Estudo', 'Produto', 'Lote', 'Data', '5 Dias', '15 Dias', 'Usuário', 'Retirada 5 Dias', 'Analista 5 Dias', 'Retirada 15 Dias', 'Analista 15 Dias', 'Justificativa 5 dias',  'Justificativa 15 dias'])
            return df
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
        finally:
            if conn:
                conn.close()

        ## REGISTROS
    def inserir_registros(self, data_hora, evento, usuario):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()

            c.execute("INSERT INTO registros (data, evento, usuario) VALUES (?, ?, ?)", (data_hora, evento, usuario))
            conn.commit()

        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
            return None
        finally:
            if conn:
                conn.close()
        
    def selecionarLOG(self, data_inicio, data_fim, usuario, texto):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()
            if texto and usuario:
                sqlite_select_query = f"""SELECT id, data, evento, usuario FROM registros 
                                      WHERE data BETWEEN '{data_inicio} 00:00:00' AND '{data_fim} 23:59:59' 
                                      AND usuario LIKE '%{usuario}%'
                                      AND evento LIKE '%{texto}%'"""
                c.execute(sqlite_select_query)
                registros = c.fetchall()
            elif texto:
                sqlite_select_query = f"""SELECT id, data, evento, usuario FROM registros 
                                      WHERE data BETWEEN '{data_inicio} 00:00:00' AND '{data_fim} 23:59:59' 
                                      AND evento LIKE '%{texto}%'"""
                c.execute(sqlite_select_query)
                registros = c.fetchall()
            elif usuario:
                sqlite_select_query = f"""SELECT id, data, evento, usuario FROM registros 
                                      WHERE data BETWEEN '{data_inicio} 00:00:00' AND '{data_fim} 23:59:59' 
                                      AND usuario LIKE '%{usuario}%'"""
                c.execute(sqlite_select_query)
                registros = c.fetchall()
            else:
                sqlite_select_query = f"""SELECT id, data, evento, usuario FROM registros 
                                      WHERE data BETWEEN '{data_inicio} 00:00:00' AND '{data_fim} 23:59:59'"""
                c.execute(sqlite_select_query)
                registros = c.fetchall()
            conn.close()

            df = pd.DataFrame(registros, columns=['Id', 'Data', 'Registro', 'Usuário'])
            df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d %H:%M:%S')
            df['Data'] = df['Data'].dt.strftime('%d-%m-%y %H:%M:%S')
            return df
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
            return None
        finally:
            if conn:
                conn.close()

    def enviarEmail(self, subject, body):
        try:
            # Configurações do servidor SMTP
            smtp_server = 'smtp.office365.com'
            smtp_port = 587
            sender = "sistemashypera@outlook.com"
            password = "Infohypera1234@"
            
            recipients = ["amanda.borges@brainfarma.ind.br", "andressa.maciel@brainfarma.ind.br", "eliane.tomaz@brainfarma.ind.br", "fernanda.sales@brainfarma.ind.br", "fernanda.fonseca@brainfarma.ind.br", "fernando.resende@brainfarma.ind.br", "gabriel.severino@brainfarma.ind.br", "gabriela.clemente@brainfarma.ind.br", "giovannasilva@brainfarma.ind.br", "havila.costa@brainfarma.ind.br", "laysse.gomes@brainfarma.ind.br", "lucas.o.souza@brainfarma.ind.br", "luisa.mello@brainfarma.ind.br", "paulo.g.almeida@brainfarma.ind.br", "vinni.vianna@brainfarma.ind.br", "vitor.franca@brainfarma.ind.br"]
            
            # Criar a mensagem de e-mail
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = f'Estabilidade de Excursão - {subject}'
            
            msg.attach(MIMEText(body, 'plain'))
            
            try:
                # Configurar socket com timeout
                socket.setdefaulttimeout(10)
                # Conectar ao servidor SMTP e enviar e-mail
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(sender, password)
                    server.send_message(msg)
                    return 'sucesso'                    
            except (socket.timeout, smtplib.SMTPException) as e:
                print(f'Falha ao enviar e-mail: {e}')
                return None
            except Exception as e:
                print(f'Erro inesperado: {e}')
                return None
        except Exception as e:
            print(f"Ocorreu uma exceção: {e}") 
            return None
        finally:
            self.inserir_registros(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"E-mail enviado para: {recipients}", self.usuario)

