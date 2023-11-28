from inhabitant import Inhabitant
class Human(Inhabitant):

    def __init__(self, name, age=0, energy=0):
        self.name = name
        self.age = age
        self.energy = energy

    clothing = []

    def dress(self, clothing):
        pass

    def undress(self, clothing):
        pass

    def __repr__(self):
      return f"Human(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
      return f"Human name: {self.name}, age={self.age}, energy: {self.energy}"


if __name__ == "__main__":

    # create an object of type Human
    human = Human("Brad")

    # display the current state of the object
    print(repr(human))

    # invoke the method move on the object
    human.move(10)
