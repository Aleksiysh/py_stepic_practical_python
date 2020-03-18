

def get_objects_by_coords(position):
    rez = []
    for g_object in game_objects:
        if game_objects.get(g_object).get('position') == position:
            rez.append(g_object)
    return rez


def remove_objects():
    global old_objects
    for key in old_objects:
        game_objects.pop(key, None)
    old_objects.clear()


def player_interaction(player, obj):
    if 'coin' in obj:
        old_objects.append(obj)


def wave_interaction(wave, obj):
    if 'player' in obj or 'soft_wall' in obj:
        old_objects.append(obj)


def move_objects():
    for move in movements:
        to_point = get_objects_by_coords(move[1])
        flag = True
        if to_point:
            for point in to_point:
                if not game_objects[point]['passable']:
                    flag = False
                    break
                if flag:
                    game_objects[move[0]]['position'] = move[1]
                    interactions.append((point, move[0]))
        else:
            game_objects[move[0]]['position'] = move[1]
    movements.clear()


def add_new_objects():
    for obj in new_objects:
        if is_passble(obj[2]):
            position = obj[2]  # if len(obj)==3 else (None, None)
            key = (obj[0], get_next_counter_value()
                   ) if obj[0] != 'player' else (obj[0],)
            game_objects[key] = obj[1]
            game_objects[key].update({'position': position})
        objs = get_objects_by_coords(obj[2])
        if len(objs) > 1:
            if game_objects[objs[0]]['interactable'] and game_objects[objs[0]]['interactable']:
                interactions.append(objs[0])
                interactions.append(objs[1])


def is_passble(position):
    rez = True
    objects = get_objects_by_coords(position)
    for obj in objects:
        if not game_objects[obj]['passable']:
            rez = False
            break
    return rez


objects_ids_counter = 0


def get_next_counter_value():
    global objects_ids_counter
    result = objects_ids_counter
    objects_ids_counter += 1
    return result


def create_object(type, position, **kwargs):
    desc = {'position': position,
            'passable': type not in ['wall', 'soft_wall'],
            'interactable': type not in ['wall'],
            'char': obj_types_to_char[type]
            }
    if type == 'player':
        desc['coins'] = 0
    if type == 'bomb':
        desc['power'] = 3
        desc['life_time'] = 3
    desc.update(kwargs)
    return type, desc, position


def load_level(level):
    i = 0
    level.strip()
    game_objects.clear()
    lines = level.splitlines()
    if '' in lines:
        lines.remove('')
    for line in lines:
        for j in range(len(line.strip())):
            if line[j] != ' ':
                new_objects.append(create_object(
                    search_type(line[j]), (i, j)))
        i += 1
    add_new_objects()
    new_objects.clear()
    pass


def search_type(simbol):
    for type in obj_types_to_char:
        if obj_types_to_char[type] == simbol:
            return type


obj_types_to_char = {
    "player": "@", "wall": '#', 'soft_wall': '%', 'heatwave': '+', "bomb": '*', "coin": '$'
}

game_objects = {}
old_objects = []
movements = []
interactions = []
new_objects = []


level_example ='''
'''

load_level(level_example)
print(get_objects_by_coords((0, 0)))
pass


