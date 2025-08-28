import mysql.connector

class GetConn:
    def __init__(self, db_config):
        self.db_config = db_config

    def __enter__(self):
        # Cria a conexão
        self.conn = mysql.connector.connect(**self.db_config)
        # Cria o cursor
        self.cursor = self.conn.cursor()
        return self  # retorna a instância para usar conn e cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Fecha cursor e conexão automaticamente
        self.cursor.close()
        self.conn.close()
