from db.execute_query import execute_query
from db.get_connection import get_connection_to_db
from loger import create_loger
from typing import Optional

def add_photo_func (photos):
    """
    Функция апдейтит базу фотками
    :param data:
    передайте переменную с текущим дампом фото
    :return:
    заполняет таблицу фото
    """
    loger = create_loger(add_photo_func.__name__)
    if photos:
        with open ('db/insert_photos.sql') as q1:
            insert_photo: str = q1.read()
            execute_query(insert_photo, data=photos)
            loger.info('Data was loaded successfully')
    else:
        loger.info("No data given to func, can't update db")