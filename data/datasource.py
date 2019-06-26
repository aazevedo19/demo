import sqlite3


class Datasource:

    def getConexao(self):

        try:
            conn = sqlite3.connect('data/demo.db')
        except sqlite3.Error as e:
            print('sqlite error: ', e.args[0])  # column name is not unique
        return conn
