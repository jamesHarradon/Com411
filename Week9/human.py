class Human:
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"human(name={self.name}, age={self.age})"

    def __str__(self):
        return f"Human {self.name} is {self.age} years old."

    def grow(self):
        self.age += 1

    def eat(self, amount):
        if self.energy + amount > 100:
            print(f"Energy is {self.energy}. Cannot exceed Max Energy of {self.MAX_ENERGY}")
        self.energy += amount

    def move(self, distance):
        if self.energy - distance < 0:
            print(f"Energy is {self.energy}. Cannot reduce energy to below 0")


if __name__ == "__main__":
    human = Human()
    human.display()
    print(repr(human))
    print(human)
