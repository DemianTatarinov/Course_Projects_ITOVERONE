# Задача№1
# Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму
# Задача№2
# Выведите статистику частности букв в кортеже
# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,
# 'и', 'и', 'т', 'т', 'а', 'и', 'и',
# 'и', 'и', 'и', 'т', 'и’)
# Примечание: Статистика частности - число повторений каждой из букв.

# a = 0,1,2,3,4,5,6,7,8,9
# print(sum(a))

long_word = (
    'т', 'т', 'а', 'и', 'и', 'а', 'и',
    'и', 'и', 'т', 'т', 'а', 'и', 'и',
    'и', 'и', 'и', 'т', 'и'
)

print("Повтор букв",long_word.count('т',))
print("Повтор букв",long_word.count('а',))
print("Повтор букв",long_word.count('и',))