

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


def idle_logic(_):
    pass


def bomb_logic(bomb_object):
    if game_objects[bomb_object]['life_time'] == 0:
        old_objects.append(bomb_object)
        x = game_objects[bomb_object]['position'][0]
        y = game_objects[bomb_object]['position'][1]
        for i in (-1, 1):
            new_objects.append(
                ('heatwave', {'passable': True, 'interactable': True}, (x + i, y)))
            new_objects.append(
                ('heatwave', {'passable': True, 'interactable': True}, (x, y+i)))
        new_objects.append(
            ('heatwave', {'passable': True, 'interactable': True}, (x, y)))
    else:
        game_objects[bomb_object]['life_time'] -= 1
    pass


def heatwave_logic(heatwave):
    old_objects.append(heatwave)


object_logics = {
    'bomb': bomb_logic,
    'heatwave': heatwave_logic
}


def process_objects_logic():
    for game_object in game_objects:
        object_logics.get(game_object[0], idle_logic)(game_object)


obj_types_to_char = {
    "player": "@", "wall": '#', 'soft_wall': '%', 'heatwave': '+', "bomb": '*', "coin": '$'
}


def check_game_state():
    lose = True
    win = True

    for obj in game_objects:
        if obj[0] == 'player':
            lose = False
        if obj[0] == 'coin':
            win = False
        pass

    if lose:
        return 'lose'
    elif win:
        return 'win'
    return 'in_progress'


game_objects = {}
old_objects = []
movements = []
interactions = []
new_objects = []

level_example = """
##########
#@  %    #
#   %    #
#  %%%   #
# %%$%%  #
#  %%%   #
#   %*   #
#   %    #
#   %    #
##########
"""

load_level(level_example)
a = check_game_state()
pass
