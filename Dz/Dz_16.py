# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых более 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова
a = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 5.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

d = {i: a[i] for i in a.keys() if not ' ' in i}
print(d)

# print(sum(songsdict.values()))
# b = list(a.items())
# b.pop(0)
# b.pop(1)
# b.pop(1)
# b.pop(2)
# b.pop(2)
# b.pop(2)
# print(b)
# print(type(b))