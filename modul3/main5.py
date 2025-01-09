def get_multiplied_digits(str_number : int):
    str_number = str(str_number)
    first = int(str_number[0])
    if first > 1:
        return first * int(get_multiplied_digits(str_number[1:]))
    elif first != 0:
        return first
    else:
        return 1


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)