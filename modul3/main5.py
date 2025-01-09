def get_multiplied_digits(str_number):
    first = int(str_number[0])
    if first == 0:
        t = int(str_number[1:])
        first = first + t
    elif len(str_number) <= 1:
        return first
    else:
        t = int(get_multiplied_digits(str_number[1:]))
        return first * t


result = get_multiplied_digits('40203')
print(result)
result2 = get_multiplied_digits('402030')
print(result2)