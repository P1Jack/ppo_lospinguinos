import requests
import json
import numpy as np
from datetime import datetime


def get_rooms_numbers(windows_for_room: dict, windows: list[int], date: int):
    windows_for_room_list = sorted(list(windows_for_room.items()), key=lambda x: x[0])
    windows_for_room_list = [i for _, i in windows_for_room_list]
    height = len(windows_for_room_list)
    l, width = len(windows), sum(windows)
    arr = np.arange(1, l * height + 1).reshape(height, l)[::-1].tolist()

    for idx, level in enumerate(arr):
        new_line = []
        for j, i in enumerate(windows):
            new_line += [level[j]] * i
        arr[idx] = new_line

    light_coordinates = []
    rooms = set()
    for idx, level in enumerate(windows_for_room_list[::-1]):
        for j, condition in enumerate(level):
            if condition:
                light_coordinates.append((idx, j))
                rooms.add(arr[idx][j])

    rooms = list(rooms)
    rooms.sort()

    return arr, light_coordinates, rooms, len(rooms), date


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

    d_json = json.dumps(d)
    return d_json


print(test_rooms_correct([1, 2, 4, 6, 7, 8, 11, 12], 8, 1674594000))

response = requests.get(
    "https://olimp.miet.ru/ppo_it_final/date",
    headers={"X-Auth-Token": "ppo_11_30013"},
)


print(response.json())


