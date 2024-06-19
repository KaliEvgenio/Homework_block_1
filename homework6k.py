my_dict={'Антон':34, 'Петр':25, 'Олег':37}
print(my_dict)
print('Антон',my_dict['Антон'])
print('Jhon',my_dict.get('Jhon'))
my_dict.update({'Валентин':45, 'Константин':22,'Петр':26})
print(my_dict)
print('Антон',my_dict.pop('Антон'))
print(my_dict)

my_set={2,3, 3.23, "Пингвин", (245,33.23), 3.23, 56}
print(my_set)
my_set.update((4,3,5))
print(my_set)
my_set.discard(3.23)
print(my_set)



