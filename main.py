from get_data import get_all_photo_func
from db.add_photo import add_photo_func





if __name__ == "__main__":
    res: list = get_all_photo_func()
    add_photo_func(res)