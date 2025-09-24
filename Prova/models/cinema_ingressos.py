from datetime import datetime
from mysql.connector import connect, Error

from config import db_config


def get_cursor(dictionary: bool = True):
    try:
        conn = connect(**db_config)
        cursor = conn.cursor(dictionary=dictionary)
        return conn, cursor
    except Error as e:
        print(f"Erro ao conectar no banco: {e}")
        raise


class Ingresso:
    @staticmethod
    def get_ingressos():
        try:
            conn, cursor = get_cursor()
            cursor.execute("SELECT *, DATE_FORMAT(data_filme, '%d/%m/%Y') as data_filme FROM cinema.cinema_ingressos ORDER BY data_filme ASC")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar ingressos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
        
    @staticmethod
    def excluir_ingresso(id: int):
        try:
            conn, cursor = get_cursor()
            cursor.execute("DELETE FROM cinema.cinema_ingressos WHERE id = %s", (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar ingressos: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def get_ingresso(id: int):
        try:
            conn, cursor = get_cursor()
            cursor.execute("SELECT * FROM cinema.cinema_ingressos WHERE id = %s", (id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar ingresso: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def create_ingresso(nome_filme: str, genero: str, sessoes: str, nome_cliente: str, assento: str, data_filme: datetime) -> bool:
        try:
            conn, cursor = get_cursor()
            cursor.execute(
                """
                    INSERT INTO cinema.cinema_ingressos (nome_filme, genero, sessoes, nome_cliente, assento, data_filme)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (nome_filme, genero, sessoes, nome_cliente, assento, data_filme)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao criar ingresso: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def update_ingresso(id: int, nome_filme: str, genero: str, sessoes: str, nome_cliente: str, assento: str, data_filme: datetime) -> bool:
        try:
            conn, cursor = get_cursor()
            cursor.execute(
                """
                    UPDATE cinema.cinema_ingressos SET nome_filme = %s, genero = %s, sessoes = %s, nome_cliente = %s, assento = %s, data_filme = %s WHERE id = %s
                """,
                (nome_filme, genero, sessoes, nome_cliente, assento, data_filme, id)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar ingresso: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
        
