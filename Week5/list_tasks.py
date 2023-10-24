def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


def run_task1():
    print(directions())


# the below code ensures that the function is only called when the file is executed directly
# and not when it is imported into another module
if __name__ == "__main__":
    run_task1()