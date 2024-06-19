immutable_var=(0, 0.046, 'Строка')
print(type(immutable_var),' элементы:', immutable_var)
# тут я немного выпендрюсь
try:
    immutable_var[0]=1
except Exception as e:
    print(type(e),e,'\nОбъект класса \'tuple\' не поддерживает операцию присвоения своим элементам')

mutable_var=[0, 0.046, 'Строка']
print(type(mutable_var),' элементы:', mutable_var)
mutable_var[0]=1
print(type(mutable_var),' элементы:', mutable_var)
