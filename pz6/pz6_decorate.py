# -*- coding: utf-8 -*-
def my_decorator(func):
    def somethin2(*args, **kwargs):
        text_som = func(*args, **kwargs)
        return text_som.split()
    return somethin2

@my_decorator
def somethin(text_som):
    return text_som

name, last_name = somethin("Alexandr Kirichenko")
print(f"name = {name}")
print(f"last_name = {last_name}")