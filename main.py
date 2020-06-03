from get_data import get_all_photo_func
from db.add_photo import add_photo_func
from photo_export import create_local_copy_photo





if __name__ == "__main__":
    res: list = get_all_photo_func()
    add_photo_func(res)
    create_local_copy_photo()