
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


class Appointment:
    @staticmethod
    def get_appointments():
        try:
            with get_cursor() as cursor:
                cursor.execute("SELECT * FROM nc_appointments")
                return cursor.fetchall()
        except Exception as e:
            logger.exception(f"Erro ao buscar consultas: {e}")
            return []

    @staticmethod
    def create_appointment(patient: str, doctor: str, specialty: str, date: str) -> bool:
        try:
            with get_cursor() as cursor:
                cursor.execute(
                    """
                        INSERT INTO nc_appointments (nome_paciente, nome_medico, especialidade, data_consulta)
                        VALUES (%s, %s, %s, %s)
                    """,
                    (patient, doctor, specialty, date)
                )
            return True
        except Exception as e:
            logger.exception(f"Erro ao criar consulta: {e}")
            return False
