# -*- coding: utf-8 -*-


class Main():

    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def greeting():
        return 'hello ! I am ' + self.name + ' and I am ' + str(self.age) + ' years old!'
