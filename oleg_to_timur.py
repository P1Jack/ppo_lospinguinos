def oleg_to_timur(rooms_light, data, floor_count, rooms_count):
    ret = [data, floor_count, list(), rooms_light, len(rooms_light)]
    for i in range(rooms_count):
        if i in rooms_light:
            ret[2].append((True, i))
        else:
            ret[2].append((False, i))
    return ret

