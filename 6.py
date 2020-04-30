# Задание 6

import codecs

list = []
file = codecs.open('6.txt','r', encoding='utf-8' )

for line in file:
    list.append(line)

i = 0
file.close()
old_list = list
new_list = []
for predmet in list:
    predmet = predmet.split(':')
    name = predmet[0]
    hours = predmet [1]
    hours = hours.split()
    print(name)
    while ('—') in hours:
        hours.remove('—')
    for el in hours:
        el = el.split('(')
        el.pop()
        i = i + int(el[0])
    hours = i
    print(hours)
    new_list.append(name)
    new_list.append(hours)
    i = 0

new_list = {new_list[i]: new_list[i + 1] for i in range(0, len(new_list), 2)}
print(new_list)