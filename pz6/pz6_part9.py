# -*- coding: utf-8 -*-
# Напишите класс, который принимает список людей с интерфейсом добавления новых и при
# итерации возвращал имена людей

class People:
    def __init__(self, people=None):
        if people is None:
            self.people = []
        else:
            self.people = people

    def add_person(self, name):
        if isinstance(name, str):
            self.people.append(name)
        elif isinstance(name, list):
            self.people += name
        else:
            raise ValueError("Введите список или строку")

    def __iter__(self):
        return iter(self.people)


def main():
    group = People(["Alice", "Grum"])

    group.add_person("Ivan")
    group.add_person("Diana")
    group.add_person(['Mari', 'Eva'])

    for person in group:
        print(person)

if __name__ == '__main__':
    main()