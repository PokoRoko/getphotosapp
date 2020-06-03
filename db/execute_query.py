import sqlite3
from loger import create_loger
from typing import Optional



def get_connection_to_db(db_name: str = 'getphotosapp.db') -> sqlite3.Connection:
    """
    - создает базу данных getphotosapp.db или присоединяется к ней, если она создана
    - возвращает объект sqlite3.Connection
    - особенность в том, что соединение происходит с учетом объявленных типов.
    - добавлена поддержка ненативного типа list с помощью конвертера и адаптера
    """
    loger = create_loger(get_connection_to_db.__name__)

    with sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES) as connection:
        loger.debug('Created connection to db')
        sqlite3.register_adapter(list, lambda x: ','.join(map(lambda y: str(y), x)))
        return connection


def create_db():
    """
    Функция создания БД
    :return:
    возвращает ошибку в случае неуспеха
    """
    db_create_loger = create_loger(create_db.__name__)
    connection = get_connection_to_db()
    with connection as c:
        cursor = c.cursor()
        with open('./db/create_table_query.sql') as q1:
            create_table_db: str = q1.read()
            cursor.execute(create_table_db)
            db_create_loger.info('DataBase created')



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
        if query.startswith('INSERT'):
            cursor.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='photos' """)
            if cursor.fetchone()[0]==0:
                create_db()
        if query.startswith('SELECT'):
            try:
                cursor.execute(query)
            except sqlite3.Error as e:
                db_loger.error(e)
                c.rollback()
                return
            else:
                return cursor.fetchall()
        try:
            cursor.executemany(query, data)
        except sqlite3.Error as e:
            db_loger.error(e)
            c.rollback()
            return
        else:
            c.commit()