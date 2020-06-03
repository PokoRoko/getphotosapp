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
    default_dict: dict = {
                        'album_id':'',
                        'date':'',
                        'id' :'',
                        'owner_id':'',
                        'has_tags':'',
                        'height':'',
                        'photo_1280':'',
                        'photo_130':'',
                        'photo_604':'',
                        'photo_75':'',
                        'photo_807':'',
                        'post_id':'',
                        'text':'',
                        'width':'',
                        'photo':''
                         }
    bigest_photo_size: int = 0
    num_list: list = []
    for i in photos:
        for key in i.keys():
            if 'photo' in str(key):
                word_list: list = key.split('_')
                num_list = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)]
        bigest_photo_size = max(num_list)
        try:
            response = requests.get(i['photo_' + str(bigest_photo_size)])
            i['photo'] = response.content
        except:
            loger.info("Can't upload photo")
    if photos:
        for i in photos:
            for key in default_dict.keys():
                if key not in i.keys():
                    i.setdefault(key, '')
        with open ('db/insert_photos.sql') as q1:
            insert_photo: str = q1.read()
            try:
                execute_query(insert_photo, data=photos)
                loger.info('Data was loaded successfully')
            except:
                loger.error('Error while executing SQL query')
    else:
        loger.info("No data given to func, can't update db")