a = [1,2,3,'hello','world']
b = [1,2,3,4,5,6,7]
a.append(7)#добавляе в текс символ в конец списка
a.insert(1,7)#добавляет нужную цифру и смещает список в право
a[1]=3#заменить нужную цифру через счёт индеса
c = a+b#тот же вариант что. только создали новую переменную
b.extend(a)#дополним элементы с одного спика в другой
# print(a)
# a.remove()#удаляет только с аргументом. только с символ со страки только первую цифру которую встретит
# a.pop()#удоляет позицию в списке если оставить пустые скобки то удолит с конца списка элемент
print(a.count(3))#выводит количесво встречаемых елементов заданной цифры
d = a.copy()
d.append(5)
a.append(3)
print(d)
a.clear()
print(a)
# print(b)
# print



f= [1,12,3,4,5,16,79]
f.reverse()
f.sort()#сортирует по возрастанию
#f.sort(reverse=true) сортирует по убыванию
print(f)