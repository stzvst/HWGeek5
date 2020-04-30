# Задание 2




my_list = ['vgbhn\n', 'rgg\n', 'gfvdeerff\n', 'wesrgg\n' ]
with open("2.txt", 'w') as file_obj:
    file_obj.writelines(my_list)


with open("2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += 1
        letters = len(line)-1
        print ("В строке",  letters, "букв(ы)")
    print("Всего", lines, "строки")
