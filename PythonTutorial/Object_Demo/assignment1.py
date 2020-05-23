class Fruit(object):

    def __init__(self):
        print("This is the fruit class")

    def nutrition(self):
        print("Fruits have so many Nutrition")

    def fruit_shape(self):
        print("Every fruit shape is different")

class Apple(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("Apple is the child class of fruit")

    def nutrition(self):

        print("An Apple a day keeps doctor away")

    def color(self):
        print("Apple's colour is Red")

f = Fruit()
f.nutrition()
f.fruit_shape()

a = Apple()
a.nutrition()
a.color()
