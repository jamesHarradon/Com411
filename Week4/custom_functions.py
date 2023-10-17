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