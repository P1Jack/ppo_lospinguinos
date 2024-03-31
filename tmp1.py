import random
import time


contex = []

date = random.randint(0, 2000000000)
date = time.ctime(date).split()
date_table = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
date = f'{date[2]}-{date_table.index(date[1]) + 1}-{date[4]}'

floors = random.randint(1, 10)

windows_format = []
comnat_na_atag = random.randint(1, 10)
for i in range(comnat_na_atag):
    for _ in range(random.randint(1, 5)):
        windows_format.append(i)
windows = len(windows_format)


lights = set()
coords = []
for floor in range(floors):
    for ind, window in enumerate(windows_format):
        if random.randint(1, 100000) % 2 == 1:
            lights.add(floor * comnat_na_atag + window + 1)
            coords.append((floor, ind))


count = len(lights)


wall = []
for floor in range(floors):
    aaaaa = list()
    for window in windows_format:
        aaaaa.append(floor * comnat_na_atag + window + 1)
    wall.append(aaaaa.copy())

wall.reverse()
contex = [date, floors, windows, lights, count, wall, coords]
print(*contex, sep="\n")
# print("comnat na atag", comnat_na_atag)
# print(windows_format)
