import os
from datetime import datetime as dt

import psycopg2
import requests
from dotenv import load_dotenv

from config import config

# Получение переменных
dot_env = os.path.join('', '.env')
load_dotenv(dotenv_path=dot_env)
API_KEY = os.getenv('API_KEY')


def get_currency_rate(title: str, base_currency: str, to_currency: str):
    """Функция запрашивать актуальные курсы валют с внешнего API и сохраняет их в базе данных."""

    # Получение параметров для подключения к БД
    params = config()

    # Настройки для работы с API
    url = "https://api.apilayer.com/exchangerates_data/latest"
    param = {
        "symbols": to_currency,
        "base": base_currency,
    }
    response = requests.get(url, headers={'apikey': API_KEY}, params=param)

    # Если запрос выполнен успешно
    if response.ok:

        # Получение данных из запроса
        response_result = response.json()
        timestamp = dt.fromtimestamp(response_result.get('timestamp'))
        code = response_result.get('base')
        currency = list(response_result.get('rates').keys())[0]
        rate = list(response_result.get('rates').values())[0]
        if not timestamp or not code or not currency or not rate:
            return 'Что-то пошло не так. Попробуйте еще раз.'

        # Подключение к базе данных
        conn = psycopg2.connect(dbname='plastilin', **params)
        try:
            with conn:
                with conn.cursor() as cur:
                    # Добавление курса валют
                    cur.execute(
                        """
                        INSERT INTO converter (title, code, currency, rate, date_added)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        (title, code, currency, rate, timestamp))
        finally:
            conn.close()

        return 'Данные успешно добавлены!'

    return 'Что-то пошло не так. Попробуйте еще раз.'


def get_latest_currencies():
    """Функция возвращает дату и время последнего обновления курсов в базе данных."""

    # Получение параметров для подключения к БД
    params = config()

    # Подключение к БД
    conn = psycopg2.connect(dbname='plastilin', **params)
    db_data = None
    try:
        with conn:
            with conn.cursor() as cur:
                # Получение последних курсов валют
                cur.execute(
                    """
                    SELECT DISTINCT ON (code, currency)
                    code, currency, MAX(date_added)
                    FROM converter
                    GROUP BY code, currency
                    """,
                )
                if not db_data:
                    db_data = cur.fetchall()
    finally:
        conn.close()

    if not db_data:
        return 'В базе данных ничего нет.'

    result = ''
    for data in db_data:
        result += f'Курс валют {data[0]} на {data[1]} актуален на {data[2]}\n'

    return result


def get_currency_rate_from_db(base_currency: str, to_currency: str, amount: int | float) -> str:
    """Функция принимает две валюты (base_currency и to_currency) и сумму для конвертации. Возвращает результат
    конвертации на основе актуальных курсов валют из базы данных."""

    # Получение параметров для подключения к БД
    params = config()

    # Подключение к БД
    conn = psycopg2.connect(dbname='plastilin', **params)
    db_data = None
    try:
        with conn:
            with conn.cursor() as cur:
                # Конвертация
                cur.execute(
                    """
                    SELECT code, currency, rate, date_added
                    FROM converter
                    WHERE code='{0}' AND currency='{1}'
                    ORDER BY date_added DESC
                    """.format(base_currency, to_currency)
                )
                if not db_data:
                    db_data = cur.fetchone()

    finally:
        conn.close()

    if not db_data:
        return 'В базе данных ничего нет.'
    result = f'{amount} {db_data[0]} = {db_data[2] * amount} {db_data[1]}\n'

    return result
