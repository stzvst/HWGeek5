# Задание 5


file = open("5.txt", 'w')
print ('Введите числа через пробелы')
chisla = input()
chisla = chisla.split()


for el in chisla:
    file.write(el + "\n")


file.close()
my_list = []
file = open('5.txt', 'r')
for line in file:
    my_list.append(int(line))
print(my_list)
print("Сумма всех чисел будет равна:",sum(my_list))