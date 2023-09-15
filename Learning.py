def update_dictionary(d, key, value):
    if key in d:
        d[key] = d.get(key, []) + [value]
        return
    if key not in d:
        d[key * 2] = d.get(key * 2, []) + [value]
        return
    if d[key * 2] not in d:
        d[key * 2] = [value]
        return