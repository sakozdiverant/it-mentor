# Создайте словарь содержащий данные о человеке. В качестве строковых ключей используйте
# его имя, возраст, пол, рост, вес, размер ноги.
def create_person():
    return {
        "имя": "Балавах",
        "возраст": 50,
        "пол": "мужской",
        "рост": 160,  # в сантиметрах
        "вес": 60  # в килограммах
    }

def add_shoe_size(person, size):
    person["размер ноги"] = size
    return person

def remove_age(person):
    del person["возраст"]
    return person

def get_person_data(person):
    return person.items()
