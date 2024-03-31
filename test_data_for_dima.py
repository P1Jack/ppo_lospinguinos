import random
import time
from oleg_to_timur import oleg_to_timur


rooms_light = []
data = random.randint(0, 2000000000)
floor_count = random.randint(1, 10)
rooms_count = floor_count * random.randint(1, 10)
for i in range(rooms_count):
    rooms_light.append((i, random.randint(0, 1000000) % 2 == 1))

ret = oleg_to_timur(rooms_light, data, floor_count, rooms_count)
print(ret)
