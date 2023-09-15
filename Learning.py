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

x = {}
    
print(update_dictionary(x, 0, -5))  # None
print(x)# {0: [-5]}  (0*0=2)
update_dictionary(x, 1, -1)
print(x)# {0: [-5], 2: [-1]} (тк индекса 1 нет создаем key*2=2)
update_dictionary(x, 2, -2)
print(x)# {0: [-5], 2: [-1, -2]} (тк индекс 2 есть добавляем -2 в него)
update_dictionary(x, 3, -3)
print(x)# 0: [-5], 2: [-1, -2], 6: [-3]}
