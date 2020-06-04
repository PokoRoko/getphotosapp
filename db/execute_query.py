import sqlite3
from loger import create_loger
from typing import Optional

def execute_query(query: str, data=None) -> Optional[list]:
    """
    функция пробует исполнить sql запрос:
    - sql выражение
    - connection - объект соединения с бд по дефолту - это соединение с нашей бд
    - data - данные которые надо вставить, по дефолту = None

    возвращает список кортежей если используется SELECT.
    При использовании SELECT комментарии нужно указывать после SQL выражения из-за startswith
    """
    data: Optional[dict] = {} if data is None else data
    if query.startswith('INSERT'):
        _if_db_not_exist()
        _execute_many(query, data)
    if query.startswith('SELECT'):
        res: list = _execute_for_select(query)
        return res

def _get_connection_to_db(db_name: str = 'getphotosapp.db') -> sqlite3.Connection:
    """
    - создает базу данных getphotosapp.db или присоединяется к ней, если она создана
    - возвращает объект sqlite3.Connection
    - особенность в том, что соединение происходит с учетом объявленных типов.
    - добавлена поддержка ненативного типа list с помощью конвертера и адаптера
    """
    loger = create_loger(_get_connection_to_db.__name__)

    with sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES) as connection:
        loger.debug('Created connection to db')
        sqlite3.register_adapter(list, lambda x: ','.join(map(lambda y: str(y), x)))
        return connection

def _create_db():
    """
    Функция создания БД
    :return:
    возвращает ошибку в случае неуспеха
    """
    db_create_loger = create_loger(_create_db.__name__)
    connection = _get_connection_to_db()
    with connection as c:
        cursor = c.cursor()
        with open('./db/create_table_query.sql') as q1:
            create_table_db: str = q1.read()
            cursor.execute(create_table_db)
            db_create_loger.info('DataBase created')
        return

def _execute_for_select(query):
    """
    Функция для селекта, так как
    :param query:
    :return:
    """
    db_loger = create_loger(_execute_for_select.__name__)
    connection = _get_connection_to_db()
    with connection as c:
        cursor = c.cursor()
        try:
            cursor.execute(query)
        except sqlite3.Error as e:
            db_loger.error(e)
            c.rollback()
            return
        else:
            return cursor.fetchall()

def _execute_many(query: str, data: Optional):
        db_loger = create_loger(_execute_many.__name__)
        connection = _get_connection_to_db()
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
        return

def _if_db_not_exist():
    db_loger = create_loger(_if_db_not_exist.__name__)
    connection = _get_connection_to_db()
    with connection as c:
        cursor = c.cursor()
        cursor.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='photos' """)
        if cursor.fetchone()[0]==0:
            _create_db()
        return