from get_data import get_all_photo_func
from db.add_photo import add_photo_func





if __name__ == "__main__":
    res: dict = get_all_photo_func()
    # for value in res.values():
    #     for keys,values in value.items():
    #         if 'items' in keys:
    #             photos = values[0]
    a = {k2:v2 if 'items' in v2.values() else None for k2,v2 in {k1: v1 for k1,v1 in res.items()}}
    ko = [
        values
        if 'items' in keys
        else None
        for keys,values in a.items()
    ]
    print(ko)
    add_photo_func(photos)

