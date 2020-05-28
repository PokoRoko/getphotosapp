import sqlite3
from db.get_connection import get_connection_to_db
from loger import create_loger
from typing import Optional

"""
TODO:
* Сейчас использование SELECT запросов возможно только в том случае если:
- до слова SELECT нет никаких символов
- SELECT написано большими буквами
Необходимо добавить более гибкое поведение.
"""


def execute_query(query: str, data=None) -> Optional[list]:
    """
    функция пробует исполнить sql запрос:
    - sql выражение
    - connection - объект соединения с бд по дефолту - это соединение с нашей бд
    - data - данные которые надо вставить, по дефолту = None

    возвращает список кортежей если используется SELECT.
    При использовании SELECT комментарии нужно указывать после SQL выражения из-за startswith
    """
    db_loger = create_loger(execute_query.__name__)
    data: Optional[dict] = {} if data is None else data
    connection = get_connection_to_db()
    with connection as c:
        cursor = c.cursor()
        try:
            cursor.executemany(query, data)
        except sqlite3.Error as e:
            db_loger.error(e)
            c.rollback()
            return
        else:
            c.commit()
        if query.startswith('SELECT'):
            return cursor.fetchall()


if __name__ == '__main__':
    """
    Тестирование работы функции.
    """
    with open('../db/create_table_query.sql') as query:
        execute_query(query.read())
