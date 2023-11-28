import robot
import human
class Planet:
    def __init__(self, name):
        self.inhabitants = []
        self.name = name

    def add_inhabitant(self, inhabitant_obj):
        self.inhabitants.append(inhabitant_obj)

    def remove_inhabitant(self, inhabitant_obj):
        self.inhabitants.append(inhabitant_obj)

    def __repr__(self):
        return f"Planet(name={self.name}, inhabitants={self.inhabitants})"

    def __str__(self):
        return f"Planet name: {self.name}, Inhabitants: {self.inhabitants}"


if __name__ == "__main__":
    planet = Planet("Tattooine")
    human = human.Human("Derek")
    robot = robot.Robot("Terminator")
    planet.add_human(human)
    planet.add_robot(robot)
    print(planet)
    print(repr(planet))
