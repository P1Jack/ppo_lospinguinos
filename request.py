import requests
import numpy as np


def get_rooms_numbers(windows_for_room: dict, windows: list[int]):
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

    return arr, light_coordinates, rooms, len(rooms)


print(get_rooms_numbers({
            "floor_1": [
                False,
                True,
                False,
                True,
                False,
                False
            ],
            "floor_2": [
                True,
                False,
                True,
                False,
                False,
                True
            ],
            "floor_3": [
                False,
                False,
                True,
                False,
                True,
                False
            ],
            "floor_4": [
                False,
                False,
                False,
                True,
                False,
                True
            ]
        }, [
            3,
            2,
            1
        ]))


response = requests.get(
    "https://olimp.miet.ru/ppo_it_final",
    params={"X-Auth-Token": "ppo_10_17605"},
)


print(response.json())


