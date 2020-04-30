# Задание 6


import json


pribil_firm_info = []
pribil_firms = []
all = []

i = 0


with open("7.txt", 'r') as file:
    for line in file:
        name, type, money, izderj = line.split()
        pribil = int(money) - int(izderj)
        if pribil > 0:
            print (name, 'с формой собственности', type, '. Выручка:', money, ', издержки:',izderj, '. Прибыль составляет:', pribil )
            pribil_firm_info.append(pribil)
            pribil_firms.append(name)
            pribil_firms.append(pribil)


        else:
            print(name, 'с формой собственности', type, '. Выручка:', money, ', издержки:', izderj,
                  '. Убыток составляет:', pribil)
            pribil_firms.append(name)
            pribil_firms.append(pribil)

pribil_firm = 0
for el in pribil_firm_info:
    pribil_firm = el + int(pribil_firm)
    i += 1

sred = pribil_firm/i
print ('Средняя прибыль составляет:', sred)
name = ('average_profit')

avegage =  {name: str(sred)}

pribil_firms = {pribil_firms[i]: pribil_firms[i + 1] for i in range(0, len(pribil_firms), 2)}

all.append(pribil_firms)
all.append(avegage)

print(all)

with open('7.json', 'w') as write_js:
    json.dump(all, write_js)
    json_str = json.dumps(all)
    print('В JSON пишем:' ,json_str)


