

def get_objects_by_coords(position):
    rez = []
    for g_object in game_objects:
        if game_objects.get(g_object).get('position') == position:
            rez.append(g_object)
    return rez


def remove_objects():
    # global old_objects
    for key in old_objects:
        game_objects.pop(key, None)
    old_objects.clear()


def player_interaction(player, obj):
    if 'coin' in obj:
        old_objects.append(obj)


def wave_interaction(wave, obj):
    if 'player' in obj or 'soft_wall' in obj:
        old_objects.append(obj)


game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'},
    ('coin', 2): {'position': (1, 3), 'passable': True, 'interactable': True, 'char': '$'}
}
