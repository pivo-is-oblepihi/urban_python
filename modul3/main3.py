def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [22, 'eeee', 25.5]
values_dict = {"a":'www', "b":23, "c":17.3}
values_list_2 = [25.3, 'a']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)