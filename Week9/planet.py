import robot
import human
class Planet:
    def __init__(self, name):
        self.humans = []
        self.robots = []
        self.name = name

    def add_human(self, human_obj):
        self.humans.append(human_obj)

    def remove_human(self, human_obj):
        self.humans.remove(human_obj)

    def add_robot(self, robot_obj):
        self.robots.append(robot_obj)

    def remove_robot(self, robot_obj):
        self.robots.remove(robot_obj)

    def __repr__(self):
        return f"Planet(name={self.name}, humans={self.humans}, robots={self.robots}"

    def __str__(self):
        return f"Planet name: {self.name}, Humans: {self.humans}, Robots: {self.robots}"


if __name__ == "__main__":
    planet = Planet("Tattooine")
    human = human.Human("Derek")
    robot = robot.Robot("Terminator")
    planet.add_human(human)
    planet.add_robot(robot)
    print(planet)
    print(repr(planet))
