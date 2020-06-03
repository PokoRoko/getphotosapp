import os
from db.execute_query import execute_query
from loger import create_loger

def _create_photo_folders():
    """
    Служебная функция создания фоток и файлов
    :return:
    папки созданы локально в проекте.
    """
    path: str = './photos'
    folder_name: str = 'test1'
    folders: dict = _get_folders()
    for f in folders:
        name: str = ('album' + str(f[0]))
        fullpath = os.path.join(path, name)
        if not os.path.exists(fullpath):
            os.makedirs(fullpath)

def _get_folders():
    """
    Получаем список альбомов из БД
    для создания архитектуры с папками локально
    :return:
    """
    loger = create_loger(_get_folders.__name__)
    with open('db/select_albums.sql') as q1:
        select_albums: str = q1.read()
        try:
            res= execute_query(select_albums)
            loger.info('Albums data exported successfully')
            return res
        except:
            loger.error('Error while executing SQL query')

def create_local_copy_photo():
    """
    фунция создания файлов локально, с фотографиями
    :return:
    файлы созданы как результат выполнения функции
    """
    loger = create_loger(create_local_copy_photo.__name__)
    _create_photo_folders()
    with open('db/select_photos.sql') as q1:
        select_photo: str = q1.read()
        try:
            res= execute_query(select_photo)
            loger.info('Photos data exported successfully')
        except:
            loger.error('Error while executing SQL query')
        for r in res:
            path: str = './photos/' + 'album' + str(r[0]) + '/photo' + str(r[1]) + '.jpeg'
            with open(path, 'wb') as file:
                file.write(r[3])
                file.close()