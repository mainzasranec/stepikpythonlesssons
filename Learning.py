def update_dictionary(d, key, value):
    if d[key] in d:
        d[key] = [value]
        return
    if d[key] not in d:
         d[2] = [value]
         return
    if d[2] not in d:
        d[2] = [value]
        return

d = {}
print (update_dictionary(d, 1, -1))