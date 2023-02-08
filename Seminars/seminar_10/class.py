class Person:
    def __init__(self, name, rost, color):
        self.name = name
        self.rost = rost
        self.color = color

    def say_hello(self):
        print(f'Меня зовут {self.name}, мой рост {self.rost} сантиметров')


ivan = Person("ivan", 190, "brown")
vasya = Person("vasya", 182, "green")

ivan.say_hello()
