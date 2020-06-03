import logging
import os


def create_loger(name: str, level: int = 20):
    """
    функция генерирует объект логера по запросу.
    на вход принимает название логера
    нужна, чтобы создавать отдельные логеры для каждой функции и понимать откуда пришла ошибка
    """

    if not os.path.exists('./logs'):
        os.makedirs('./logs')
    loger = logging.getLogger(name)
    loger.setLevel(level)
    fh = logging.FileHandler('logs/getphotosapp.log')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    loger.addHandler(fh)
    loger.addHandler(ch)
    return loger

