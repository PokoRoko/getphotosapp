import sqlite3
from loger import create_loger


def get_connection_to_db(db_name: str = 'getphotosapp.db') -> sqlite3.Connection:
    """
    - создает базу данных tracking_robot.db или присоединяется к ней, если она создана
    - возвращает объект sqlite3.Connection
    - особенность в том, что соединение происходит с учетом объявленных типов.
    - добавлена поддержка ненативного типа list с помощью конвертера и адаптера
    """
    loger = create_loger(get_connection_to_db.__name__)

    with sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES) as connection:
        loger.debug('Created connection to db')
        sqlite3.register_adapter(list, lambda x: ','.join(map(lambda y: str(y), x)))
        return connection