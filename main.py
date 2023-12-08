from currencies import get_currency_rate, get_latest_currencies, get_currency_rate_from_db
from db_operations import Connector


def main():
    """
    Функция для взаимодействия с пользователем.
    """
    # Создание экземпляра класса для подключения к postgresql
    database = Connector()

    # Создание базы данных "plastilin"
    database.create_db('plastilin')

    # Создание таблицы "converter" в базе данных "plastilin"
    database.create_tables('plastilin')
    # Приветственное сообщение
    print("""Данный скрипт вносит в базу данных актуальный курс валют и позволяет производить их конвертацию.""")
    print("МЕНЮ:")
    print(
        "-----\n1. Добавить в базу данных новый курс валют.\n2. Посмотреть дату и время последнего обновления."
        "курса валют.\n3. Конвертация между валютами.\n4. Выход.")

    # Взаимодействие с пользователем
    user_answer = input("Введите выбранный пункт: ")
    while user_answer not in ('1', '2', '3', '4'):
        user_answer = input("Повторно введите выбранный пункт: ")

    # Добавление в базу данных новый курс валют
    if user_answer == '1':
        while True:

            # Взаимодействие с пользователем
            print("Добавление курса валют:")
            print("------------------------\n1. Добавить.\n2. Посмотреть дату и время последнего обновления.\n"
                  "3. Конвертация между валюта.\n4. Выход.")
            user_answer_adder = input("Введите выбранный пункт: ")
            while user_answer_adder not in ('1', '2', '3', '4'):
                user_answer_adder = input("Повторно введите выбранный пункт: ")

            # Добавление курса валют в базу данных
            if user_answer_adder == '1':
                user_title = input("Введите название для курса валют: ").title()
                user_code = input("Введите актуальный курс валют: ").upper()
                while user_code.upper() not in ('USD', 'CNY', 'EUR', 'GBP'):
                    user_code = input("Введите валюту из списки - ['CNY', 'GBP', 'USD', 'EUR']: ")
                user_currency = input("Введите актуальная целевую валюту : ").upper()
                while user_currency.upper() not in ('USD', 'CNY', 'EUR', 'GBP'):
                    user_currency = input("Введите валюту из списки - ['CNY', 'GBP', 'USD', 'EUR']: ")
                print(get_currency_rate(user_title, user_code, user_currency))

            # Посмотреть дату и время последнего обновления курса валют
            elif user_answer_adder == '2':
                print(get_latest_currencies())

            # Конвертация между валютами
            elif user_answer_adder == '3':
                user_base_currency = input("Введите исходную валюту: ").upper()
                while user_base_currency.upper() not in ('USD', 'CNY', 'EUR', 'GBP'):
                    user_base_currency = input("Введите исходную валюту из списки - ['CNY', 'GBP', 'USD', 'EUR']: ")
                user_to_currency = input("Введите целевую валюту : ").upper()
                while user_to_currency.upper() not in ('USD', 'CNY', 'EUR', 'GBP'):
                    user_to_currency = input("Введите целевую валюту из списки - ['CNY', 'GBP', 'USD', 'EUR']: ")
                user_amount = input("Введите сумму для конвертации: ")
                while not user_amount.isdigit():
                    user_amount = input("Введите сумму для конвертации повторно: ")
                user_amount_digit = int(user_amount)
                print(get_currency_rate_from_db(user_base_currency, user_to_currency, user_amount_digit))

            # Выход из программы
            elif user_answer_adder == '4':
                return

    # Посмотреть дату и время последнего обновления курса валют
    elif user_answer == '2':
        print(get_latest_currencies())

    # Конвертация между валютами
    elif user_answer == '3':
        user_base_currency = input("Введите исходную валюту: ").upper()
        while user_base_currency.upper() not in ('USD', 'CNY', 'EUR', 'GBP'):
            user_base_currency = input("Введите исходную валюту из списки - ['CNY', 'GBP', 'USD', 'EUR']: ")
        user_to_currency = input("Введите целевую валюту : ").upper()
        while user_to_currency.upper() not in ('USD', 'CNY', 'EUR', 'GBP'):
            user_to_currency = input("Введите целевую валюту из списки - ['CNY', 'GBP', 'USD', 'EUR']: ")
        user_amount = input("Введите сумму для конвертации: ")
        while not user_amount.isdigit():
            user_amount = input("Введите сумму для конвертации повторно: ")
        user_amount_digit = int(user_amount)
        print(get_currency_rate_from_db(user_base_currency, user_to_currency, user_amount_digit))

    # Выход из программы
    elif user_answer == '4':
        return


if __name__ == '__main__':
    main()
