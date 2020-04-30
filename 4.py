# Задание 4



translate = {"One" : "Odin", "Two" : "Dva", "Three" : 'Tri', "Four" : 'Chetire'}

file_edit = []


file = open("4.txt", "r")
for line in file:
    new_line = line.split(' - ')
    print (new_line)
    if new_line[0] in translate:

        new_word = translate[new_line[0]]
        new_word = new_word + (' - ') + new_line[1]
        file_edit.append(new_word)

print(file_edit)

file.close()

file = open("4.1", "w")
for list in file_edit:

      file.write(list + '\n')