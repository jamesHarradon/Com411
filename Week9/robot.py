from inhabitant import Inhabitant

class Robot(Inhabitant):

    laws = ""

    def __init__(self, name, age=0, energy=0):
        self.name = name
        self.age = age
        self.energy = energy


    def the_laws(self):
        pass

    def __repr__(self):
      return f"Robot(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
      return f"Robot name: {self.name}, age={self.age}, energy: {self.energy}"


if __name__ == "__main__":

    # create an object of type Human
    robot = Robot("Jeff")

    # display the current state of the object
    print(repr(robot))

    # invoke the method move on the object
    robot.move(10)
