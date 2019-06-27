import sqlite3
from data.datasource import Datasource


class PessoaController:

    def insert(self, pessoa):

        conn = Datasource().getConexao()

        c = conn.cursor()

        pessoas = [
            (pessoa.cpf, pessoa.nome, pessoa.endereco, pessoa.complemento, pessoa.cidade, pessoa.bairro,
             pessoa.estado, pessoa.cep, pessoa.dtainc),
        ]

        try:
            sql = '''INSERT INTO cadpessoa (cpf, nome, endereco, complemento, cidade, bairro, estado, cep, dtainc) 
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            c.executemany(sql, pessoas)
            conn.commit()
        except sqlite3.Error as e:
            print('sqlite error: ', e.args[0])  # column name is not unique
            return -1
        finally:
            conn.close()

        return 0
