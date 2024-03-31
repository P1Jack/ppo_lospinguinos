import time


def oleg_to_timur(rooms_light, data, floor_count, rooms_count):
    data = time.ctime(data).split()
    data_table = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    data = f'{data[2]}-{data_table.index(data[1]) + 1}-{data[4]}'

    ret = [data, floor_count, list(), rooms_light, len(rooms_light)]
    for i in range(rooms_count):
        if i in rooms_light:
            ret[2].append((True, i))
        else:
            ret[2].append((False, i))
    return ret


