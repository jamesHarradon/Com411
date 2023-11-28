class Inhabitant:

    MAX_ENERGY = 100

    def grow(self):
        self.age += 1

    def eat(self, amount):
        if self.energy + amount > 100:
            print(f"Energy is {self.energy}. Cannot exceed Max Energy of {self.MAX_ENERGY}")
        self.energy += amount

    def move(self, distance):
        if self.energy - distance < 0:
            print(f"Energy is {self.energy}. Cannot reduce energy to below 0")

    def display(self):
        print(f"I am {self.name}")



