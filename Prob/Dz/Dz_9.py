# Введи список, отсортируй его и
# оставь только уникальные элементы
# Примечание: Уникальные элементы -
# это элементы, которые появляются
# только один раз в списке


numbers = [1,1,4,5,6,7,7]
list = [e for e in set(numbers) if numbers.count(e) == 1]
print(list)






# numbers = [1,1,4,5,6,7,7]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)

# numbers = [1, 2, 2, 3, 3, 4, 5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)