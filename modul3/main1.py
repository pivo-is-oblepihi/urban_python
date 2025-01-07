calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info(s):
    tuple_ = (len(s), s.upper(), s.lower())
    count_calls()
    return tuple_

def is_contains(st, list_to_search):
    count_calls()
    st = st.upper()
    uppercase_list = [i.upper() for i in list_to_search]
    if st in uppercase_list:
        return 1
    else:
        return 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)