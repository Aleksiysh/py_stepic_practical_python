

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
                    interactions.append((point,move[0]))
        else:
            game_objects[move[0]]['position'] = move[1]
    movements.clear()


game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'},
    ('coin', 2): {'position': (1, 2), 'passable': True, 'interactable': True, 'char': '$'}
}

old_objects = []
movements = []
interactions = []

movements = [(('player', ), (0, 1))]
move_objects()
game_objects[('player', )]['position'] == (1, 1)

movements = [(('player', ), (1, 2))]
move_objects()
game_objects[('player', )]['position'] == (1, 2)
