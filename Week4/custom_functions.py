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