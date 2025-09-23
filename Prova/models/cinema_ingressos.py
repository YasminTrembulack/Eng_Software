from datetime import datetime
from loguru import logger
from typing import Generator
from contextlib import contextmanager
from mysql.connector import connect, Error
from mysql.connector.cursor import MySQLCursorDict

from config import db_config


@contextmanager
def get_cursor(dictionary: bool = True) -> Generator[MySQLCursorDict, None, None]:
    conn = None
    cursor = None
    try:
        conn = connect(**db_config)
        cursor = conn.cursor(dictionary=dictionary)
        yield cursor
        conn.commit()
    except Error as e:
        logger.exception(f"Erro ao conectar no banco: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


class Ingresso:
    @staticmethod
    def get_ingressos():
        try:
            with get_cursor() as cursor:
                cursor.execute("SELECT *, DATE_FORMAT(data_filme, '%d/%m/%Y') as data_filme FROM cinema.cinema_ingressos ORDER BY data_filme ASC")
                return cursor.fetchall()
        except Exception as e:
            logger.exception(f"Erro ao buscar ingressos: {e}")
            return []
        
    @staticmethod
    def excluir_ingresso(id: int):
        try:
            with get_cursor() as cursor:
                cursor.execute("DELETE FROM cinema.cinema_ingressos WHERE id = %s", (id,))
            return True
        except Exception as e:
            logger.exception(f"Erro ao deletar ingressos: {e}")
            return False
    
    @staticmethod
    def get_ingresso(id: int):
        try:
            with get_cursor() as cursor:
                cursor.execute("SELECT * FROM cinema.cinema_ingressos WHERE id = %s", (id,))
                return cursor.fetchone()
        except Exception as e:
            logger.exception(f"Erro ao buscar ingresso: {e}")
            return None

    @staticmethod
    def create_ingresso(nome_filme: str, genero: str, sessoes: str, nome_cliente: str, assento: str, data_filme: datetime) -> bool:
        try:
            with get_cursor() as cursor:
                cursor.execute(
                    """
                        INSERT INTO cinema.cinema_ingressos (nome_filme, genero, sessoes, nome_cliente, assento, data_filme)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (nome_filme, genero, sessoes, nome_cliente, assento, data_filme)
                )
            return True
        except Exception as e:
            logger.exception(f"Erro ao criar ingresso: {e}")
            return False
    
    @staticmethod
    def update_ingresso(id: int, nome_filme: str, genero: str, sessoes: str, nome_cliente: str, assento: str, data_filme: datetime) -> bool:
        try:
            print(id)
            with get_cursor() as cursor:
                cursor.execute(
                    """
                       UPDATE cinema.cinema_ingressos SET nome_filme = %s, genero = %s, sessoes = %s, nome_cliente = %s, assento = %s, data_filme = %s WHERE id = %s
                    """,
                    (nome_filme, genero, sessoes, nome_cliente, assento, data_filme, id)
                )
            return True
        except Exception as e:
            logger.exception(f"Erro ao atualizar ingresso: {e}")
            return False
        
