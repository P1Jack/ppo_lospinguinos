import requests
import json
import numpy as np
from datetime import datetime


def get_rooms_numbers(windows: dict, windows_for_room: list[int], date: int):
    windows_list = sorted(list(windows.items()), key=lambda x: x[0])
    windows_list = [i for _, i in windows_list]
    height = len(windows_list)
    l, width = len(windows_for_room), sum(windows_for_room)
    arr = np.arange(1, l * height + 1).reshape(height, l)[::-1].tolist()

    for idx, level in enumerate(arr):
        new_line = []
        for j, i in enumerate(windows_for_room):
            new_line += [level[j]] * i
        arr[idx] = new_line

    light_coordinates = []
    rooms = set()
    for idx, level in enumerate(windows_list[::-1]):
        for j, condition in enumerate(level):
            if condition:
                light_coordinates.append((idx, j))
                rooms.add(arr[idx][j])

    rooms = list(rooms)
    rooms.sort()

    result = {
        "home": arr,
        "light": light_coordinates,
        "rooms": rooms,
        "count": len(rooms),
        "date": date,
        "correct": test_rooms_correct(rooms, len(rooms), date),
        "height": len(arr),
        "width": len(arr[0])
    }

    return result


def test_rooms_correct(rooms: list[int], number: int, date: int):
    from_timestamp = datetime.fromtimestamp(date).strftime("%d-%m-%Y")
    from_timestamp = from_timestamp.split("-")
    yy = from_timestamp[-1][-2:]
    from_timestamp = from_timestamp[0] + "-" + from_timestamp[1] + "-" + yy
    d = {
        "data": {
            "count": number,
            "rooms": rooms
        },
        "date": from_timestamp
    }

    url = "https://olimp.miet.ru/ppo_it_final"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": "ppo_10_17608"
    }

    response = requests.post(url, data=json.dumps(d), headers=headers)
    return response.status_code == 200


def get_data_from_date(date: str):
    day, month, year = date.split("-")
    response = requests.get(
        "https://olimp.miet.ru/ppo_it_final",
        headers={"X-Auth-Token": "ppo_11_30013"},
        params={
            "day": day,
            "month": month,
            "year": year
        }
    )

    body = response.json()["message"]
    windows_for_flat = body["windows_for_flat"]["data"]
    windows = body["windows"]["data"]
    date = body["date"]["data"]
    return get_rooms_numbers(windows, windows_for_flat, date)


print(get_data_from_date("25-01-23"))
