# -*- coding: utf-8 -*-
# Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс
# и какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton

class Dog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Dog, cls).__new__(cls)
        return cls._instance

    def __init__(self, name, breed, age):
        if not hasattr(self, 'initialized'):
            self.name = name
            self.breed = breed
            self.age = age
            self.initialized = True

    def voice(self):
        return "Gaf!"

    def fetch(self, item):
        return f"{self.name} is fetching the {item}!"

    def info(self):
        return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}"

#dog3 = Dog("Tuzik", "Haski", 2)
dog1 = Dog("Sharik", "Golden Retriever", 5)
print(dog1.info())
print(dog1.voice())
print(dog1.fetch("ball"))

dog2 = Dog("Max", "Labrador", 3)
print(dog2.info())

print(dog1 is dog2)

dog2.age = 6
print(dog2.info())