import requests
from requests.exceptions import HTTPError
from loger import create_loger
from settings import key


def get_all_photo_func() -> dict:
    """
    Функция запроса всех фотографий с вашей страницы
    :key - ключ авторизации для вашего приложения, должен быть в окружении.
    :return:
    Возвращает rawdata от метода
    """
    error_log = create_loger(get_all_photo_func.__name__)
    error_log.debug('Starting to collect data from function')
    url: str = 'https://api.vk.com/method/photos.getAll?v=5.52&access_token=' + str(key)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        error_log.error(f'Function failed because of this: {http_err}')
    except Exception as err:
        error_log.error(f'Function failed because of this: {err}')
    else:
        print('Success!')
        error_log.debug('Requested successfully')
    res: dict = response.json()
    return res['response']['items']
