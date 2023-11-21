import robot
import human
class Planet:
    def __init__(self, name):
        self.inhabitants = {
            "humans": [],
            "robots": []
        }
        self.name = name

    def add_human(self, human_obj):
        self.inhabitants["humans"].append(human_obj)

    def remove_human(self, human_obj):
        self.inhabitants["humans"].append(human_obj)

    def add_robot(self, robot_obj):
        self.inhabitants["robots"].append(robot_obj)

    def remove_robot(self, robot_obj):
        self.inhabitants["robots"].remove(robot_obj)

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
