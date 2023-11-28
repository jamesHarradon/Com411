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
            planet.add_inhabitant(human)

        for j in range(rand_num()):
            robot = Robot(f"Robot{j}")
            planet.add_inhabitant(robot)

        self.planets.append(planet)

    def show_populations(self, selection):
        total_humans = 0
        total_robots = 0
        for planet in self.planets:
            for inhabitant in planet.inhabitants:
                if isinstance(inhabitant, Human): total_humans += 1
                if isinstance(inhabitant, Robot): total_robots += 1
        print(f"Found {total_humans} humans and {total_robots} robots.")



universe = Universe()
universe.generate()

print(universe.planets[0].inhabitants)

