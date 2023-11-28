from planet import Planet
from robot import Robot
from human import Human
import random

class Universe:

    planets = []

    def generate(self):
        planet = Planet("Arakis")
        def rand_num():
            return round(random.random() * 10)

        for i in range(rand_num()):
            human = Human(f"Human{i}")
            planet.add_human(human)

        for j in range(rand_num()):
            robot = Robot(f"Robot{j}")
            planet.add_robot(robot)

        self.planets.append(planet)


universe = Universe()
universe.generate()

print(universe.planets[0].inhabitants)