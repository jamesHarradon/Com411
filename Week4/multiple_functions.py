def display_ladder(steps):
    stepsNum = int(steps)
    for x in range(0, stepsNum, 1):
        print("| |")
        print("***")
    print("| |")

def create_ladder():
    steps = input("How many steps in the ladder? ")
    display_ladder(steps)

create_ladder()