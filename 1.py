# Задание 1


my_file = open("1.txt", "w")
print ("Вводите строки\n Когда закончите, введите пустую строку")
text = 1
while text:
    text = input()
    if text:
        my_file.write(text + "\n" )
    else:
        continue
my_file.close()
my_file = open("1.txt", "r")
#my_f = open("text.txt", "r")
text = my_file.readlines()
print(text)
my_file.close()