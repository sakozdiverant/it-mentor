
def get_first_and_third_elements(lst):
    return lst[0], lst[2], lst[:3]

def fix_city_name(city):
    city[1] = "-"
    return city

def split_letters_and_numbers(mixed_list):
    letters = []
    numbers = []
    for item in mixed_list:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            letters.append(item)
    return letters, numbers

def modify_letters_list(letters):
    letters.pop()
    letters.reverse()
    return letters

def convert_list_to_set(lst):
    return set(lst)
