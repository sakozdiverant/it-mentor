# -*- coding: utf-8 -*-
class PersonNew:
    def __init__(self, full_name):
        self.full_name = full_name

    @property
    def full_name(self):
        if self._middle_name is None:
            return f"{self._first_name} {self._last_name}"
        else:
            return f"{self._first_name} {self._last_name} {self._middle_name}"

    @full_name.setter
    def full_name(self, name):
        if len(name.split()) == 3:
            self._first_name, self._last_name, self._middle_name = name.split()
        else:
            self._first_name, self._last_name = name.split()
            self._middle_name = None

person_new = PersonNew("Кириченко Александр Валерьевич")
print(person_new.full_name)
