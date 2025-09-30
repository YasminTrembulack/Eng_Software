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


class Tarefa:
    @staticmethod
    def get_tasks():
        try:
            with get_cursor() as cursor:
                cursor.execute("SELECT *, DATE_FORMAT(created_at, '%d/%m/%Y %H:%i:%s') as created_at FROM backend_development.tasks ORDER BY created_at ASC")
                return cursor.fetchall()
        except Exception as e:
            logger.exception(f"Erro ao buscar tarefas: {e}")
            return []
        
    @staticmethod
    def excluir_task(id: int):
        try:
            with get_cursor() as cursor:
                cursor.execute("DELETE FROM backend_development.tasks WHERE id = %s", (id,))
            return True
        except Exception as e:
            logger.exception(f"Erro ao deletar tarefa: {e}")
            return False
    
    @staticmethod
    def get_task(id: int):
        try:
            with get_cursor() as cursor:
                cursor.execute("SELECT * FROM backend_development.tasks WHERE id = %s", (id,))
                return cursor.fetchone()
        except Exception as e:
            logger.exception(f"Erro ao buscar tarefa: {e}")
            return None

    @staticmethod
    def create_task(title: str, description: str, priority: str, status: str = 'pending') -> bool:
        try:
            with get_cursor() as cursor:
                cursor.execute(
                    """
                        INSERT INTO backend_development.tasks (title, description, status, priority)
                        VALUES (%s, %s, %s, %s)
                    """,
                    (title, description, status, priority)
                )
            return True
        except Exception as e:
            logger.exception(f"Erro ao criar tarefa: {e}")
            return False

    @staticmethod
    def update_task(id: int, title: str, description: str, status: str, priority: str) -> bool:
        try:
            with get_cursor() as cursor:
                cursor.execute(
                    """
                       UPDATE backend_development.tasks SET title = %s, description = %s, status = %s, priority = %s WHERE id = %s
                    """,
                    (title, description, status, priority, id)
                )
            return True
        except Exception as e:
            logger.exception(f"Erro ao atualizar tarefa: {e}")
            return False
        