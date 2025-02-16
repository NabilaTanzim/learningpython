class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


ilma = Person("Ilma")
ilma.talk()

alvia = Person('Alvia')
alvia.talk()