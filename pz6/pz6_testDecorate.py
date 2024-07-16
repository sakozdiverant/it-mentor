# -*- coding: utf-8 -*-
class StringToList:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__.get(self.name, "")
        return value.split()

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        if self.name in instance.__dict__:
            del instance.__dict__[self.name]

def string_to_list(func):
    return StringToList(func)

class MyClass:
    def __init__(self, text=""):
        self.text = text

    @string_to_list
    def text(self):
        return self._text

    @string_to_list
    def text(self, value):
        self._text = value

obj = MyClass()

obj.text = "Python использует алгоритм C3-линеаризации для вычисления MRO."
print(obj.text)
