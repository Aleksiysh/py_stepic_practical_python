
def friends(pairs):
    dict_frends = {}
    for pair in pairs:
        if pair[0] not in dict_frends:
            dict_frends[pair[0]] = set()
        dict_frends[pair[0]].add(pair[1])
           
        if pair[1] not in dict_frends:
            dict_frends[pair[1]] = set()
        dict_frends[pair[1]].add(pair[0])
            
    return dict_frends


pairs = [("Ivan", "Maria"), ("Ella", "Ivan"), ("Ivan", "Oleg")]

a = friends(pairs)

pass
