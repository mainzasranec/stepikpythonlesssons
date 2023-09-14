def update_dictionary(d, key, value):
    if key in d:
        d[key] = [value]
        return
    if key not in d:
         d[2] = [value]
         return
    if d[2] not in d:
        d[2] = [value]
        return

d = {}
print (update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)