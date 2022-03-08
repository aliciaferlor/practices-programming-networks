# Object oriented programming: example of a class
class Dog:
    def __init__(self, the_name, the_age):
        self.name = the_name
        self.age = the_age

    def say_your_name(self):
        print("Im {}, and im sitting down here".format(self.name))

    def show_your_age(self):
        print("Im {} years old".format(self.age))

    def say_what_you_like(self):
        print("I like math")

    def multiply(self, first, second):
        print(f'Easy!, the multiplication is {first * second}')
        print("The sum is:", first + second)

ares = Dog("ares", 10)
ares.say_your_name()
ares.show_your_age()
ares.say_what_you_like()
ares.multiply(3,5)