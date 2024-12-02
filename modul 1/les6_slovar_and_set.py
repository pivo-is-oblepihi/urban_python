#work dict

my_dict = {'Name':'Polina', 'Nomer': 89052826725, 'Age': 19 }
print(my_dict)
print(my_dict['Name'])
my_dict['VUZ'] = 'LETI'
print(my_dict['VUZ'])
my_dict.update({'loves':'Vova', 'Nom_car': 456789})
print(my_dict.pop('Nomer'))
print(my_dict)

#work set
my_set = {1, 1, 'polina', 'polina', (1, 2, 3), (1, 2, 3)}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.discard('polina')
print(my_set)