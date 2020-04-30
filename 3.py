# Задание 3


personal = ["Petrov 40", "Ivanov 10", 'Sidorov 13', 'Nabokov 40', 'Sverdlov 36']

file_firm = open("3.txt" , "w")
for people in personal:
  file_firm.write(people + ("\n"))
file_firm.close()


file_firm = open("3.txt", 'r')


persons = file_firm.read()
persons = persons.split()
new_persons = {persons[i]: persons[i + 1] for i in range(0, len(persons), 2)}

file_firm.close()

list_per = []
pers = new_persons.items()
for per in pers:
  if int(per[1]) < 20:
    list_per.append(per)
  else:
    continue



print("Меньше 20 тыс. получают сотрудники:")
for per in list_per:
  print(per[0])

all = 0
i = 0

new_persons = new_persons.items()
for per in new_persons:
  all = int(per[1]) + all
  i +=1

endly = all/i

print ('\n \n Средний доход сотрудников составляет', endly, 'тыс. руб.')