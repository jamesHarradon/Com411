def listen():
    word = input("Please enter a word representing a sound: ")
    print(f"That was a loud {word}!")


listen()


def identify():
    see = input("What can you see? ")
    print(see)
    if see == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")

identify()


def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")


def cross_bridge(stepsCrossed):
    count = 0
    x = stepsCrossed
    while count < x :
        print("Crossed step")
        count+=1

    if count > 5:
        print("The bridge is collapsing!")
    else:
        print("we must keep going!")

cross_bridge(3)
cross_bridge(6)

def climb_ladder(stepsRemaining, stepsCrossed):
    if stepsRemaining > stepsCrossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

climb_ladder(5, 2)
climb_ladder(2, 5)

def climb_ladder_loop(stepsRemaining, stepsCrossed):
    while stepsCrossed < stepsRemaining:
        print("Still some way to go!")
        stepsCrossed += 1
    print("We are almost there!")


climb_ladder_loop(5,2)
climb_ladder_loop(2, 5)