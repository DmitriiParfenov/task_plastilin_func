# task_plastilin_func

task_plastilin_func — это решение тестового задания на позицию `python-разработчик` в компанию `Plastilin`. </br>

# Дополнительная информация

- Для получения качественного анализа программного кода введите в консоли:
```
flake8 --config .flake8
```

# Клонирование репозитория

В проекте для управления зависимостями используется [poetry](https://python-poetry.org/). </br>
Выполните в консоли: </br>

Для Windows: </br>
```
git clone git@github.com:DmitriiParfenov/task_plastilin_func.git
python -m venv venv
venv\Scripts\activate
pip install poetry
poetry install
```

Для Linux: </br>
```
git clone git@github.com:DmitriiParfenov/task_plastilin_func.git
cd database_vacancies_HH
python3 -m venv venv
source venv/bin/activate
curl -sSL https://install.python-poetry.org | python3
poetry install
```

# Работа с переменными окружения

- В проекте для получения курса валют используется [apilayer](https://apilayer.com/). </br>
- В директории `task_plastilin_func` создайте файл `.env`. Пример содержимого файла:
```
API_KEY=ваш ключ API
```
# Работа с базой данной PostgreSQL

- В директории проекта создайте файл `database.ini`. Пример содержимого файла:
```
[postgresql]
HOST=localhost
USER=postgres
PASSWORD=password
PORT
```
- В результате выполнения скрипта будет создана база данных `plastilin`. В ней будет следующая таблица:
  - `converter` - содержит курсы валют

# Запуск
- Зайдите в директорию `task_plastilin_func/main.py` и запустите скрипт.
- Следуйте инструкциям, которые выводятся в терминале.