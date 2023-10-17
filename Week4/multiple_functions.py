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


def sum_weights(charWeight, invWeight):
    return charWeight + invWeight

def calc_avg_weight(charWeight, invWeight):
    return sum_weights(charWeight, invWeight) / 2

def run():
    charWeight = int(input("What is the character weight?"))
    invWeight = int(input("What is the inventory weight?"))
    whatFunc = input("Enter either sum or average")
    if whatFunc == "sum":
        sum_weights(charWeight, invWeight)
    elif whatFunc == "average":
        calc_avg_weight(charWeight, invWeight)
    else:
        print("Invalid input. Please enter either sum or average")

run()