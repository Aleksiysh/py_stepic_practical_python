game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'}
}


def get_objects_by_coords(position):
    rez = []
    for g_object in game_objects:
        if game_objects.get(g_object).get('position') == position:
            rez.append(g_object)
    return rez


def main():
    print(get_objects_by_coords((0, 1)) == [('wall', 1)],
          get_objects_by_coords((1, 1)) == [('player',)],
          get_objects_by_coords((2, 1)) == []
          )
 


if __name__ == "__main__":
    main()
