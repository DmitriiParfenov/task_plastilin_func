import psycopg2
from psycopg2 import errors

from config import config


class Connector:
    """Класс для создания базы данных и таблиц."""

    def __init__(self) -> None:
        """
        Экземпляр инициализируется params для подключения к postgres.
        """
        self.params = config()

    def create_db(self, database_name: str) -> None:
        """Метод в качестве аргумента принимает название базы данных и создает базу данных."""

        # Подключение к существующей базе данных
        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        # Создание новой базы данных
        try:
            cur.execute(f'CREATE DATABASE {database_name}')
        except errors.DuplicateDatabase:
            pass
        finally:
            cur.close()
            conn.close()

    def create_tables(self, database_name: str) -> None:
        """Метод в качестве аргумента принимает название базы данных и создает в ней две таблицы: employers и
        db_vacancies."""

        # Подключение к базе данных
        conn = psycopg2.connect(dbname=database_name, **self.params)
        try:
            with conn:
                with conn.cursor() as cur:
                    # Создание таблицы converter
                    cur.execute("""CREATE TABLE IF NOT EXISTS converter (
                    converter_id SERIAL,
                    title VARCHAR,
                    code VARCHAR(3),
                    currency VARCHAR(3),
                    rate NUMERIC(50, 6),
                    date_added TIMESTAMP,     
                           
                    CONSTRAINT pk_converter_converter_id PRIMARY KEY (converter_id),
                    CONSTRAINT chk_converter_code_upper CHECK (UPPER(code) = code),
                    CONSTRAINT chk_converter_currency_upper CHECK (UPPER(currency) = currency),
                    CONSTRAINT chk_converter_code_actual CHECK (code in ('USD', 'EUR', 'CNY', 'GBP')),
                    CONSTRAINT chk_converter_currency_actual CHECK (currency in ('USD', 'EUR', 'CNY', 'GBP'))
                    )""")
        finally:
            conn.close()
