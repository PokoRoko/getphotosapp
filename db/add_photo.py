from db.execute_query import execute_query
from loger import create_loger
import requests

def add_photo_func(photos):
    """
    Функция апдейтит базу фотками
    :param data:
    передайте переменную с текущим дампом фото
    :return:
    заполняет таблицу фото
    """
    loger = create_loger(add_photo_func.__name__)
    data: dict = _get_photo_size(photos)
    with open('db/insert_photos.sql') as q1:
        insert_photo: str = q1.read()
        try:
            execute_query(insert_photo, data=data)
            loger.info('Data was loaded successfully')
        except:
            loger.error('Error while executing SQL query')

def _get_photo_size(data : dict) -> dict:
    loger = create_loger(_get_photo_size.__name__)
    for photo in data:
        for key in photo:
            if 'photo' in key:
                word_list: list = key.split('_')
                num_list = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)]
        bigest_photo_size= max(num_list)
        try:
            response = requests.get(photo['photo_' + str(bigest_photo_size)])
            i = response.content
            photo['photo'] = response.content
        except:
            loger.info("Can't upload photo")
    final: dict = _add_none_values(data)
    return  final

def _add_none_values(data: dict) -> dict:
    default_dict: dict = {
        'album_id': '', 'date': '', 'id': '', 'owner_id': '',
        'has_tags': '', 'height': '', 'photo_1280': '', 'photo_130': '',
        'photo_604': '', 'photo_75': '', 'photo_807': '', 'post_id': '',
        'text': '', 'width': '', 'photo': ''
                        }
    if data:
        for photo in data:
            for key in default_dict:
                if key not in photo:
                    photo.setdefault(key, '')
    return data