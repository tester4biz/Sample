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


if __name__ == '__main__':
    m = Main('taro', 30)

    print(m.get_name())
    print(m.get_age())
