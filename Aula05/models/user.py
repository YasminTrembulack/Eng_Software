import bcrypt

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


class User:
    @staticmethod
    def get_users():
        try:
            with get_cursor() as cursor:
                cursor.execute("SELECT * FROM users_mvc")
                return cursor.fetchall()
        except Exception as e:
            logger.exception(f"Erro ao buscar usuários: {e}")
            return []

    @staticmethod
    def create_user(name: str, email: str, password: str, birthday: str) -> bool:
        try:
            # gerar hash da senha
            hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

            with get_cursor() as cursor:
                cursor.execute(
                    """
                        INSERT INTO users_mvc (name, email, password, birthday)
                        VALUES (%s, %s, %s, %s)
                    """,
                    (name, email, hashed_pw.decode("utf-8"), birthday)
                )
            return True
        except Exception as e:
            logger.exception(f"Erro ao criar usuário: {e}")
            return False
