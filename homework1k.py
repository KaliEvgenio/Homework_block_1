example="Пример_строки"

#Выведите на экран(в консоль) первый символ этой строки.
print(example[0],'\n')
#Выведите на экран(в консоль) последний символ этой строки.
print(example[-1],'\n')
#Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов).
print(example[int(len(example)/2):len(example)],'\n')
#Выведите на экран(в консоль) это слово наоборот.
print(example[::-1],'\n')
#Выведите на экран(в консоль) каждый второй символ этой строки.
print(example[1::2],'\n')
